import sys
import math
import timeit
from Approximation import Approximation 
from Approximation.Instruments.Regressions import PowerMultiplyRegression
from Approximation.Instruments.Functors import X, Log2, Ceil

class GuessApproximation:
    def Analyse(parameters, results, fullSearch = True, fnIsGoodDiscripancy = None, bDebug = True):
        if(fnIsGoodDiscripancy == None):
            fnIsGoodDiscripancy = GuessApproximation.DefaultIsGoodDiscripancy_;
        
        bestDiscripancy = sys.float_info.max;
        bestRegression = [];
        bestKoefficients = [];
        parameters = GuessApproximation.UpdateParameters_(parameters);

        approximation = Approximation.Approximation(parameters, results);
        
        regressionList = [PowerMultiplyRegression.PowerMultiplyRegression];#PowerRegression.PowerRegression, 

        baseFunctorList = GuessApproximation.MakeBaseFunctorList_(parameters);
        for baseFunctor in baseFunctorList:
            for regression in regressionList:
                if not bDebug:
                    startRegressionTime = timeit.default_timer()

                for power in range(0, 20 + 1):
                    currentRegression = regression.GetRegression(baseFunctor, power);
                    
                    currentKoefficients = approximation.CalcKoefficients(currentRegression);
                    if(len(currentKoefficients) != len(currentRegression)):
                        raise Exception("Can't solve equasion");

                    currentDiscripancy = approximation.CalcDiscripancy(currentKoefficients, currentRegression);
                    

                    if(currentDiscripancy < bestDiscripancy):
                        bestDiscripancy = currentDiscripancy;
                        bestRegression = currentRegression;
                        bestKoefficients = currentKoefficients;

                    for j in range(len(bestKoefficients) - 1, -1, -1):
                        if(bestKoefficients[j] == 0):
                            bestKoefficients.pop(j);
                            
                            bestRegression.pop(j);
                    
                    if(bestDiscripancy == 0 or not fullSearch and fnIsGoodDiscripancy(bestDiscripancy)):
                        return bestKoefficients, bestRegression, bestDiscripancy;
                    
                    if not bDebug:
                        currRegressionTime = timeit.default_timer()
                        if(currRegressionTime - startRegressionTime > 5):
                            break;

        return bestKoefficients, bestRegression, bestDiscripancy;


    def DefaultIsGoodDiscripancy_(discripancy : float):
        return discripancy < 0.000001;

    def MakeBaseFunctorList_(parameters):
        baseFunctors = [];
        
        parametersWidth = len(parameters[0]);
        functorList = [];
        for i in range(parametersWidth):
            functorList.append(X.X([i]));
        baseFunctors.append(functorList);
        
        functorList = [];
        for i in range(parametersWidth):
            functorList.append(Ceil.Ceil(Log2.Log2(X.X([i])), True));
        baseFunctors.append(functorList);
        
        return baseFunctors;

    def UpdateParameters_(parameters):
        for i in range(len(parameters[0]) - 1, 0, -1):
            bNotFullRepeat = False;
            val = parameters[0][i];
            for j in range(1, len(parameters)):
                if(val != parameters[j][i]):
                    bNotFullRepeat = True;
                    break;
            if(not bNotFullRepeat):
                for j in range(0, len(parameters)):
                    parameters[j].pop(i);
        return parameters;