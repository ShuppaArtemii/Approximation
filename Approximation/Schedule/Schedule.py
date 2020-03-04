import matplotlib.pyplot as plt   
from matplotlib.widgets import TextBox
from mpl_toolkits.mplot3d import Axes3D 
from Approximation import FunctorListMethods
import decimal
import numpy

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)
    
class Graph:
    def __init__(self, graphPlot,  koefficients, functions, minX, maxX, minY, maxY, title = ''):
        self.graphPlot = graphPlot;
        self.SetParameters(koefficients, functions, minX, maxX, minY, maxY);
        self.title = title;
        self.Update()

    def SetKoefficientsAndFunctions(self, koefficients, functions):
        self.koefficients = koefficients;
        self.functions = functions;
        
        uniqueConformities = [];
        for i in range(len(functions)):
            for j in range(len(functions[i].conformity_)):
                value = functions[i].conformity_[j];
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

    def SetParameters(self, koefficients, functions, minX, maxX, minY, maxY):
        self.SetKoefficientsAndFunctions(koefficients, functions);
        self.SetRange(minX, maxX, minY, maxY);

    def UpdateXMin(self, text):
        self.minX = text;
        self.Update();
    def UpdateXMax(self, text):
        self.maxX = text;
        self.Update();
    def UpdateYMin(self, text):
        self.minY = text;
        self.Update();
    def UpdateYMax(self, text):
        self.maxY = text;
        self.Update();

    def Update(self):
        self.graphPlot.clear();
        
        if(self.dimentions == 0 or self.dimentions == 1):
            x, y = self.Get2D_Data();
            self.graphPlot.plot(x, y);
        elif(self.dimentions == 2):
            x, y, z = self.Get3D_Data();
            self.graphPlot.plot_surface(x, y, z);
            
            
        self.graphPlot.grid(True);
        plt.title(self.title)
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


def Draw(koefficients, functions, xMin, xMax, yMin, yMax, title = ""):
    uniqueConformities = [];
    for i in range(len(functions)):
        for j in range(len(functions[i].conformity_)):
            value = functions[i].conformity_[j];
            if(not value in uniqueConformities):
                uniqueConformities.append(value);
    dimentions = len(uniqueConformities);

    

    #min-max-X "area"
    minXBox = plt.axes([0.2, 0.05, 0.1, 0.05])
    maxXBox = plt.axes([0.4, 0.05, 0.1, 0.05])

    #min-max-Y "area"
    minYBox = plt.axes([0.6, 0.05, 0.1, 0.05])
    maxYBox = plt.axes([0.8, 0.05, 0.1, 0.05])

    #yourself textboxes
    minXTextBox = TextBox(minXBox, 'minX', initial=xMin, label_pad=0.05)
    maxXTextBox = TextBox(maxXBox, 'maxX', initial=xMax, label_pad=0.05)

    minYTextBox = TextBox(minYBox, 'minY', initial=yMin, label_pad=0.05)
    maxYTextBox = TextBox(maxYBox, 'maxY', initial=yMax, label_pad=0.05)
    
    #set text
    minXTextBox.text = str(xMin);
    maxXTextBox.text = str(xMax);
    minYTextBox.text = str(yMin);
    maxYTextBox.text = str(yMax);

    
    if(dimentions == 0 or dimentions == 1):
        graphPlot = plt.axes([0.1, 0.2, 0.8, 0.7])
    elif(dimentions == 2):
        graphPlot = plt.axes([0.1, 0.2, 0.8, 0.7], projection='3d')
    else:
        raise ValueError('Display multiple dimensions does not realized yet');
    g = Graph(graphPlot, koefficients, functions, minXTextBox.text, maxXTextBox.text, minYTextBox.text, maxYTextBox.text, title)
   
    #set submit
    minXTextBox.on_submit(g.UpdateXMin)
    maxXTextBox.on_submit(g.UpdateXMax)

    minYTextBox.on_submit(g.UpdateYMin)
    maxYTextBox.on_submit(g.UpdateYMax)

    plt.show()
