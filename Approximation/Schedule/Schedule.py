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
    
class Graph:
    def __init__(self, graphPlot,  koefficients, functions, parameters, results, minX, maxX, minY, maxY, title = '', legend = ''):
        self.graphPlot = graphPlot;
        self.SetParameters(koefficients, functions, parameters, results, minX, maxX, minY, maxY);
        self.title = title;
        self.legend = legend;
        self.Update()

    def SetKoefficientsAndFunctions(self, koefficients, functions):
        self.koefficients = koefficients;
        self.functions = functions;
        
        uniqueConformities = [];
        for i in range(len(functions)):
            for j in range(len(functions[i].GetConformity())):
                value = functions[i].GetConformity()[j];
                if(not value in uniqueConformities):
                    uniqueConformities.append(value);
        
        self.dimentions = len(uniqueConformities);
        if(self.dimentions > 2):
            raise ValueError('Display multiple dimensions does not realized yet');
    
    def SetRange(self, minX, maxX, minY, maxY):
        self.minX = minX;
        self.maxX = maxX;
        self.minY = minY;
        self.maxY = maxY;

    def SetParameters(self, koefficients, functions, parameters, results, minX, maxX, minY, maxY):
        self.parameters = parameters;
        self.results = results;
        self.SetKoefficientsAndFunctions(koefficients, functions);
        self.SetRange(minX, maxX, minY, maxY);

    def UpdateXMin(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.minX = text;
        self.Update();
    def UpdateXMax(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.maxX = text;
        self.Update();
    def UpdateYMin(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.minY = text;
        self.Update();
    def UpdateYMax(self, text):
        if(int(text) < 0):
            ctypes.windll.user32.MessageBoxW(0, text + ' is invalid value', 'Error', 0);
        self.maxY = text;
        self.Update();

    def Update(self):
        self.graphPlot.clear();
        if(self.dimentions == 0 or self.dimentions == 1):
            x, y = self.Get2D_Data();
            self.graphPlot.plot(x, y, label= self.legend);
            xPoints = [];
            for i in range(len(self.parameters)):
                xPoints.append(self.parameters[i][0]);
            yPoints = [];
            for i in range(len(self.results)):
                yPoints.append(self.results[i]);
            plt.scatter(xPoints, yPoints, c='r');

        elif(self.dimentions == 2):
            x, y, z = self.Get3D_Data();
            self.graphPlot.plot_surface(x, y, z, label= self.legend);

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
        plt.title(self.title);
        if(len(self.legend) < 25):
            plt.legend();
        plt.draw()
        
    def Get2D_Data(self):
        x = [];
        y = [];
        step = (int(self.maxX) + 1 - int(self.minX)) / 100;
        for i in drange(int(self.minX), int(self.maxX) + step, step):
            x.append(i);
            sum = 0;
            for j in range(len(self.functions)):
                sum += self.koefficients[j] * self.functions[j]([i]);
            y.append(sum);
        return x, y;

    def Get3D_Data(self):
        stepX = (int(self.maxX) + 1 - int(self.minX)) / 100;    
        x = numpy.arange (int(self.minX), int(self.maxX) + 1, stepX);
        stepY = (int(self.maxY) + 1 - int(self.minY)) / 100;
        y = numpy.arange (int(self.minY), int(self.maxY) + 1, stepY);
        xgrid, ygrid = numpy.meshgrid(x, y);
      
        matrix = [];

        for i in x:
            row = [];
            for j in y:
                row.append(FunctorListMethods.CalculateDependence(self.koefficients, self.functions, [i, j]));
            matrix.append(row);
        zgrid = numpy.array(matrix);
        return xgrid, ygrid, zgrid;


def Draw(koefficients, functions, parameters, results, xMin, xMax, yMin, yMax, title = "", legend = ""):
    uniqueConformities = [];
    for i in range(len(functions)):
        for j in range(len(functions[i].GetConformity())):
            value = functions[i].GetConformity()[j];
            if(not value in uniqueConformities):
                uniqueConformities.append(value);
    dimentions = len(uniqueConformities);
    if(dimentions > 2):
        raise ValueError('Display multiple dimensions does not realized yet');
    
    plt.figure(figsize=(9.6, 7.2))#set window size
    
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
        graphPlot = plt.axes([0.1, 0.2, 0.8, 0.7], projection='3d')

    g = Graph(graphPlot, koefficients, functions, parameters, results, minXTextBox.text, maxXTextBox.text, minYTextBox.text, maxYTextBox.text, title, legend)
   
    #set submit
    minXTextBox.on_submit(g.UpdateXMin)
    maxXTextBox.on_submit(g.UpdateXMax)

    minYTextBox.on_submit(g.UpdateYMin)
    maxYTextBox.on_submit(g.UpdateYMax)

    plt.show()
