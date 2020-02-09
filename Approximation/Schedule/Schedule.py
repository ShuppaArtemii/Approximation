import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot 
import numpy
import array
from Approximation import FunctorListMethods
class Schedule:
    #возвращает данные для графика
    def MakeGridData_(koefficients, functions, start, stop, step):
        x = numpy.arange (start, stop, step);
        y = numpy.arange (start, stop, step);
        xgrid, ygrid = numpy.meshgrid(x, y);
      
        matrix = [];

        for i in x:
            row = [];
            for j in y:
                row.append(FunctorListMethods.CalculateDependence(koefficients, functions, [i, j]));
            matrix.append(row);
        zgrid = numpy.array(matrix);
        return xgrid, ygrid, zgrid;
    
    #рисует график
    def Draw(koefficients, functions, start = 0, stop = 10, step = None):
        if(step == None):
            step = (stop - start) / 100;
        
        uniqueConformities = [];
        for i in range(len(functions)):
            for j in range(len(functions[i].conformity_)):
                value = functions[i].conformity_[j];
                if(not value in uniqueConformities):
                    uniqueConformities.append(value);
        
        if(len(uniqueConformities) < 2):
            y = [];
            
            for i in range(start, stop, round(step)):
                sum = 0;
                for j in range(len(functions)):
                    sum += koefficients[j] * functions[j]([i]);
                y.append(sum);
            
            fig, ax = pyplot.subplots();
            ax.plot(y);

        elif(len(uniqueConformities) == 2):
            x, y, z = Schedule.MakeGridData_(koefficients, functions, start, stop, step);
            fig = pylab.figure();
            axes = Axes3D(fig);
            axes.plot_surface(x, y, z);
        else:
            raise ValueError('Invalid parameters');
        pylab.show();
    