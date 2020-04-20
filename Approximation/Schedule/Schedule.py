import matplotlib.pyplot as plt 
from matplotlib.widgets import TextBox
from mpl_toolkits.mplot3d import Axes3D 
from Approximation import FunctorListMethods
import decimal
import numpy
import ctypes
def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)
    
class WindowGraph:
    def __init__(self, graphPlot,  koefficients, functorList, parameters, results, minX, maxX, minY, maxY, title = '', subtitle='', legend = ''):
        self.graphPlot = graphPlot;
        self.SetParameters(koefficients, functorList, parameters, results, minX, maxX, minY, maxY);
        self.title_ = title + "\n" + subtitle;
        self.legend_ = legend;
        self.Update()

    def SetKoefficientsAndFunctorList(self, koefficients, functorList):
        self.koefficients_ = koefficients;
        self.functorList_ = functorList;
        
        self.dimentions_ = len(functorList.GetConformity());
        if(self.dimentions_ > 2):
            raise ValueError('Display multiple dimensions does not realized yet');
    
    def SetRange(self, minX, maxX, minY, maxY):
        self.minX_ = minX;
        self.maxX_ = maxX;
        self.minY_ = minY;
        self.maxY_ = maxY;

    def SetParameters(self, koefficients, functions, parameters, results, minX, maxX, minY, maxY):
        self.parameters_ = parameters;
        self.results_ = results;
        self.SetKoefficientsAndFunctorList(koefficients, functions);
        self.SetRange(minX, maxX, minY, maxY);

    def UpdateXMin(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.minX_ = text;
        self.Update();
    def UpdateXMax(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.maxX_ = text;
        self.Update();
    def UpdateYMin(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.minY_ = text;
        self.Update();
    def UpdateYMax(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.maxY_ = text;
        self.Update();

    def Update(self):
        self.graphPlot.clear();
        if(self.dimentions_ == 0):
            x, y = self.Get2D_Data();
            self.graphPlot.plot(x, y, label= self.legend_);
            xPoints = [];
            conformity = 0;
            for i in range(len(self.parameters_)):
                xPoints.append(self.parameters_[i][conformity]);
            yPoints = [];
            for i in range(len(self.results_)):
                yPoints.append(self.results_[i]);
            plt.scatter(xPoints, yPoints, c='r');

        elif(self.dimentions_ == 1):
            x, y = self.Get2D_Data();
            self.graphPlot.plot(x, y, label= self.legend_);
            xPoints = [];
            conformity = self.functorList_.GetConformity()[0];
            for i in range(len(self.parameters_)):
                xPoints.append(self.parameters_[i][conformity]);
            yPoints = [];
            for i in range(len(self.results_)):
                yPoints.append(self.results_[i]);
            plt.scatter(xPoints, yPoints, c='r');

        elif(self.dimentions_ == 2):
            x, y, z = self.Get3D_Data();
            surf = self.graphPlot.plot_surface(x, y, z, label= self.legend_);
            
            #Следующие 2 строки нужны чтобы избежать ошибки: 'Poly3DCollection' object has no attribute... Это ошибка в реализации библиотеки 
            surf._facecolors2d=surf._facecolors3d;
            surf._edgecolors2d=surf._edgecolors3d;
            
            #xPoints = [];
            #for i in range(len(self.parameters)):
            #    xPoints.append(self.parameters[i][0]);
            #yPoints = [];
            #for i in range(len(self.parameters)):
            #    yPoints.append(self.parameters[i][1]);
            #zPoints = [];
            #for i in range(len(self.results)):
            #    zPoints.append(self.results[i]);
            #plt.scatter(xPoints, yPoints, zPoints, c='r');
            
        self.graphPlot.grid(True);
        plt.title(self.title_);
        if(len(self.legend_) < 25):
            plt.legend();
        plt.draw()
        
    def Get2D_Data(self):
        x = [];
        y = [];
        step = (int(self.maxX_) + 1 - int(self.minX_)) / 100;
        for i in drange(int(self.minX_), int(self.maxX_) + step, step):
            x.append(i);
            sum = 0;
            
            conformity = self.functorList_.GetConformity();
            for j in range(len(self.functorList_)):
                
                if(len(conformity) == 0):
                    sum += self.koefficients_[j] * self.functorList_[j]([]);
                else:
                    data = dict();
                    data[conformity[0]] = i;
                    sum += self.koefficients_[j] * self.functorList_[j](data);
            y.append(sum);
        return x, y;

    def Get3D_Data(self):
        stepX = (int(self.maxX_) + 1 - int(self.minX_)) / 100;    
        x = numpy.arange (int(self.minX_), int(self.maxX_) + 1, stepX);
        stepY = (int(self.maxY_) + 1 - int(self.minY_)) / 100;
        y = numpy.arange (int(self.minY_), int(self.maxY_) + 1, stepY);
        xgrid, ygrid = numpy.meshgrid(x, y);
      
        matrix = [];

        for i in x:
            row = [];
            for j in y:
                data = dict();
                conformity = self.functorList_.GetConformity();
                data[conformity[0]] = i;
                data[conformity[1]] = j;

                row.append(FunctorListMethods.CalculateDependence(self.koefficients_, self.functorList_, data));

            matrix.append(row);
        zgrid = numpy.array(matrix);
        return xgrid, ygrid, zgrid;

class Schedule:
    def __init__(self, koefficients, functorList, parameters, results, xMin=None, xMax=None, yMin=None, yMax=None, title = "", subtitle="", legend = ""):
        #Set default arguments 
        minPoint = min(parameters)[0]
        maxPoint = max(parameters)[0]
        if(minPoint == 0 and maxPoint == 0):
            minPoint = 0;
            maxPoint = 1;
        if(xMin == None): xMin = minPoint;
        if(xMax == None): xMax = maxPoint;
        if(yMin == None): yMin = minPoint;
        if(yMax == None): yMax = maxPoint;

        #Calculate and check dimentions
        dimentions = len(functorList.GetConformity());
        if(dimentions > 2):
            raise ValueError('Display multiple dimensions does not realized yet');
        
        #set window size
        plt.figure(figsize=(9.6, 7.2))
    
        #min-max-X "area"
        minXBox = plt.axes([0.2, 0.05, 0.1, 0.05])
        maxXBox = plt.axes([0.4, 0.05, 0.1, 0.05])

        #min-max-Y "area"
        minYBox = plt.axes([0.6, 0.05, 0.1, 0.05])
        maxYBox = plt.axes([0.8, 0.05, 0.1, 0.05])

        #yourself textboxes
        minXTextBox = TextBox(minXBox, 'minX', initial=xMin, label_pad=0.05)
        maxXTextBox = TextBox(maxXBox, 'maxX', initial=xMax, label_pad=0.05)
        if dimentions != 2:
            color = "#BBBBBB";
            hovercolor = color;
        else:
           color ='.95';
           hovercolor = '1';

        minYTextBox = TextBox(minYBox, 'minY', initial=yMin, label_pad=0.05, color = color, hovercolor=hovercolor )
        maxYTextBox = TextBox(maxYBox, 'maxY', initial=yMax, label_pad=0.05, color = color, hovercolor=hovercolor )
    
        #set text
        minXTextBox.text = str(xMin);
        maxXTextBox.text = str(xMax);
        minYTextBox.text = str(yMin);
        maxYTextBox.text = str(yMax);

        if dimentions != 2:
            minYTextBox.active = False;
            maxYTextBox.active = False;
    
        #if dimentions != 2:
            #minYTextBox.active = False;
            #maxYTextBox.active = False;
            #minYTextBox.;#e(state="disabled");
        #minYTextBox.label = "hi";#False;
        #minYTextBox.color = (255, 0, 0);

        if(dimentions == 0 or dimentions == 1):
            graphPlot = plt.axes([0.1, 0.2, 0.8, 0.7])
        elif(dimentions == 2):
            graphPlot = plt.axes([0.1, 0.15, 0.8, 0.8], projection='3d')

        g = WindowGraph(graphPlot, koefficients, functorList, parameters, results, minXTextBox.text, maxXTextBox.text, minYTextBox.text, maxYTextBox.text, title, subtitle, legend)
   
        #set submit
        minXTextBox.on_submit(g.UpdateXMin)
        maxXTextBox.on_submit(g.UpdateXMax)

        minYTextBox.on_submit(g.UpdateYMin)
        maxYTextBox.on_submit(g.UpdateYMax)

    def Show(self):
        plt.show();
    def Save(self, fileName):
        plt.savefig(fileName);
