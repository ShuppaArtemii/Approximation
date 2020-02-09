import sys
from Approximation.Instruments import Functions

from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import CeilFunctor

from Approximation import Approximation
from Approximation.Instruments.Regressions import PowerRegression
from Schedule import Schedule
class GuessApproximation:
    def Analyse(parameters, results):
        bestDiscripancy = sys.float_info.max;
        bestRegression = [];
        bestKoefficients = [];

        approximation = Approximation.Approximation(parameters, results);
        
        baseFunctors = [BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"), CeilFunctor.CeilFunctor(BaseFunctor.BaseFunctor(Functions.Log2X, [0], "log2(x)"))];
        

        for i in range(len(baseFunctors)):
            
            baseFunctorsList = [];
            parametersWidth = len(parameters[0]);
            for paramIndex in range(parametersWidth):
                functor = baseFunctors[i];
                functor.conformity_ = [paramIndex];
                functor.strFunction_ = baseFunctors[i].strFunction_ + str(i);
                baseFunctorsList.append(functor);
            
            for power in range(0, 20):
                currentRegression = PowerRegression.PowerRegression.GetRegression(baseFunctors[i], power);
                bestKoefficients, bestRegression, bestDiscripancy = GuessApproximation.AnalyseRegression_(approximation, currentRegression, bestKoefficients, bestRegression, bestDiscripancy);
                if(GuessApproximation.IsGoodDiscripancy(bestDiscripancy)):
                    break;

        return bestKoefficients, bestRegression, bestDiscripancy;

    def AnalyseRegression_(approximation, currentRegression, bestKoefficients, bestRegression, bestDiscripancy):
        currentKoefficients = approximation.CalcKoefficients(currentRegression);
        if(len(currentKoefficients) == 0):
            return bestKoefficients, bestRegression, bestDiscripancy;

        currentDiscripancy = approximation.CalcDiscripancy(currentKoefficients, currentRegression);
        
        if(currentDiscripancy < bestDiscripancy):
            bestDiscripancy = currentDiscripancy;
            bestRegression = currentRegression;
            bestKoefficients = currentKoefficients;

        for i in range(len(bestKoefficients) - 1, -1, -1):
            if(bestKoefficients[i] == 0):
                bestKoefficients.pop(i);
                bestRegression.pop(i);
        
        return bestKoefficients, bestRegression, bestDiscripancy;


    def IsGoodDiscripancy(discripancy : bool):
        return discripancy < 0.000001;

if __name__ == '__main__':
    parameters = [[11]];
    results = [22];
    koeff, funcList, disc = GuessApproximation.Analyse(parameters, results);
    Schedule.Schedule.Draw(koeff, funcList, None, 0, 10);