#import pylab
#from mpl_toolkits.mplot3d import Axes3D
#import numpy
#import array

#def frange(start, stop, step):
#	i = start
#	while i < stop:
#		yield i
#		i += step

##возвращает данные для графика
#def MakeGridData_(koefficients, functions, start, stop, step):
#    x = numpy.arange (start, stop, step);
#    y = numpy.arange (start, stop, step);
#    xgrid, ygrid = numpy.meshgrid(x, y);
  
#    matrix = [];
#    for i in range(len(xgrid)):
#        row = [];
#        for j in range(len(ygrid)):
#            sum = 0;
#            for funcIdx in range(0, len(functions)):
#                sum += koefficients[funcIdx] * functions[funcIdx]([i, j]);
#            row.append(sum);
#        matrix.append(row);
#    zgrid = numpy.array(matrix);
#    return xgrid, ygrid, zgrid;

##рисует график
#def Draw(koefficients, functions, start = -10, stop = 10, step = 0.1):
#    x, y, z = MakeGridData_(koefficients, functions, start, stop, step);
#    fig = pylab.figure();
#    axes = Axes3D(fig);
#    axes.plot_surface(x, y, z);
#    pylab.show();