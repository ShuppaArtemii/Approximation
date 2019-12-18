from Approximation.Instruments import Functions

from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import CeilFunctor

from Approximation import Approximation
from Approximation.Instruments.Regressions import PowerRegression
from Schedule import Schedule
import sys

def ShowInfo(koefficients, functorsList, discripancy):
    
    print("y = ", end='');
    if(len(koefficients) == 0 or len(functorsList) == 0):
        print('?');
    else:
        print(str(koefficients[0]), end='');
        if(functorsList[0].ToString() != ""):
            print("*" + functorsList[0].ToString(), end='');

        for i in range(1, len(functorsList)):
            print(" + " + str(koefficients[i]), end='');
            if(functorsList[i].ToString() != ""):
                print("*" + functorsList[i].ToString(), end='');
        print();

    print("Discripancy: " + str(discripancy));

class GuessApproximation:
    def Analyse(parameters, results):
        bestDiscripancy = sys.float_info.max;
        bestRegression = [];
        bestKoefficients = [];

        approximation = Approximation.Approximation(parameters, results);
        
        baseFunctors = [BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"), CeilFunctor.CeilFunctor(BaseFunctor.BaseFunctor(Functions.Log2X, [0], "log2(x)"))];
        for i in range(len(baseFunctors)):
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
    #y = 1 + log2(x0)
    parameters = [[2],[3],[4],[5],[6],[7],[8],[9],[15],[20],[25],[30],[35],[40],[45],[50],[100],[150],[200],[250],[300],[350],[400],[450],[500]];
    results = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 10, 10, 10, 10];
    
    koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, results);
    ShowInfo(koefficients, functorsList, discripancy);
    Schedule.Schedule.Draw(koefficients, functorsList, 1, 100);

    #y = 3*x0
    parameters = [[2], [3], [4], [5]];
    results = [6, 9, 12, 15];
    
    koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, results);
    ShowInfo(koefficients, functorsList, discripancy);
    Schedule.Schedule.Draw(koefficients, functorsList, 0, 100);
