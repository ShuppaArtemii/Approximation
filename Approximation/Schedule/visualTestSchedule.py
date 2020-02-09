from Approximation import GuessApproximation
import Schedule 
from Approximation import FunctorListMethods
from Approximation.Instruments import Functions
from Approximation.Instruments import Functors

if __name__ == '__main__':
    #test 11
    koefficients = [11];
    functorList = [Functors.BaseFunctor.BaseFunctor(Functions.Return1, [], "")];
    print(FunctorListMethods.GetStringDependence(koefficients, functorList));
    Schedule.Schedule.Draw(koefficients, functorList, 0, 11, 1);

    #test x
    koefficients = [1];
    functorList = [Functors.BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x")];
    print(FunctorListMethods.GetStringDependence(koefficients, functorList));
    Schedule.Schedule.Draw(koefficients, functorList, 0, 11, 1);

    #test x^2 + y^2
    koefficients = [1, 1];
    functorList = [Functors.PowerFunctor.PowerFunctor(Functors.BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x0"), 2),
                   Functors.PowerFunctor.PowerFunctor(Functors.BaseFunctor.BaseFunctor(Functions.ReturnX, [1], "x1"), 2)];
    
    print(FunctorListMethods.GetStringDependence(koefficients, functorList));
    Schedule.Schedule.Draw(koefficients, functorList, 0, 11, 1);

    #test log2(x) + log2(y)
    koefficients = [1, 1];
    functorList = [Functors.BaseFunctor.BaseFunctor(Functions.Log2X, [0], "log2(x0)"),
                   Functors.BaseFunctor.BaseFunctor(Functions.Log2X, [1], "log2(x1)")];
    
    print(FunctorListMethods.GetStringDependence(koefficients, functorList));
    Schedule.Schedule.Draw(koefficients, functorList, 1, 11, 1);
