from Approximation.Instruments import Functions

from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import CeilFunctor

from Approximation import Approximation
from Approximation.Instruments.Regressions import PowerRegression

import sys


class GuessApproximation:
    def Analyse(parameters, results, fullSearch = True, fnIsGoodDiscripancy = None):
        if(fnIsGoodDiscripancy == None):
            fnIsGoodDiscripancy = GuessApproximation.DefaultIsGoodDiscripancy_;

        bestDiscripancy = sys.float_info.max;
        bestRegression = [];
        bestKoefficients = [];
        parameters = GuessApproximation.UpdateParameters_(parameters);

        approximation = Approximation.Approximation(parameters, results);
        
        baseFunctors = GuessApproximation.MakeBaseFunctors_(parameters);
        for i in range(len(baseFunctors)):
            for power in range(0, 20):
                currentRegression = PowerRegression.PowerRegression.GetRegression(baseFunctors[i], power);
                
                currentKoefficients = approximation.CalcKoefficients(currentRegression);
                if(len(currentKoefficients) == 0):
                    return bestKoefficients, bestRegression, bestDiscripancy;

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

        return bestKoefficients, bestRegression, bestDiscripancy;


    def DefaultIsGoodDiscripancy_(discripancy : float):
        return discripancy < 0.000001;

    def MakeBaseFunctors_(parameters):
        baseFunctors = [];
        
        parametersWidth = len(parameters[0]);
        functorList = [];
        for i in range(parametersWidth):
            functorList.append(BaseFunctor.BaseFunctor(Functions.ReturnX, [i], "x" + str(i)));
        baseFunctors.append(functorList);
        
        functorList = [];
        for i in range(parametersWidth):
            functorList.append(CeilFunctor.CeilFunctor(BaseFunctor.BaseFunctor(Functions.Log2X, [i], "log2(x" + str(i) + ")")));
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