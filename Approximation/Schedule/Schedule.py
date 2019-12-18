import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
import array

class Schedule:
    #возвращает данные для графика
    def MakeGridData_(koefficients, functions, start, stop, step):
        x = numpy.arange (start, stop, step);
        y = numpy.arange (start, stop, step);
        xgrid, ygrid = numpy.meshgrid(x, y);
      
        matrix = [];

        for i in xgrid[0]:
            row = [];
            for j in xgrid[0]:
                sum = 0;
                for funcIdx in range(0, len(functions)):
                    sum += koefficients[funcIdx] * functions[funcIdx]([i, j]);
                row.append(sum);
            matrix.append(row);
        zgrid = numpy.array(matrix);
        return xgrid, ygrid, zgrid;
    
    #рисует график
    def Draw(koefficients, functions, start = 0, stop = 10, step = None):
        if(step == None):
            step = (stop - start) / 100;
        
        x, y, z = Schedule.MakeGridData_(koefficients, functions, start, stop, step);
        fig = pylab.figure();
        axes = Axes3D(fig);
        axes.plot_surface(x, y, z);
        pylab.show();
    