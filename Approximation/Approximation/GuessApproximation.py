import sys
import math
import timeit
from Approximation.Approximation import Approximation 
from Approximation.Instruments.Regressions.PowerMultiplyRegression import PowerMultiplyRegression
from Approximation import FunctorListMethods
from Approximation.Instruments.Functors.X import X
from Approximation.Instruments.Functors.Log2 import Log2
from Approximation.Instruments.Functors.Ceil import Ceil
from Approximation.Instruments.Functors.Exp import Exp
from decimal import Decimal

class GuessApproximation:
    goodDiscripancy_ = 0.000001;


    def Analyse(parameters, results, fastMode=True, fullBustMode=False, debugMode=False, baseFunctorList=None):
        for i in range(len(parameters)):
            for j in range(len(parameters[i])):
                parameters[i][j] = Decimal(parameters[i][j])
            results[i] = Decimal(results[i])

        totalBestDiscripancy = sys.float_info.max
        totalBestRegression = []
        totalBestKoefficients = []
        parameters = GuessApproximation.__SimplifyParameters(parameters)

        approximation = Approximation(parameters, results)
        
        regressionList = [PowerMultiplyRegression]
        if baseFunctorList == None:
            baseFunctorList = GuessApproximation.__MakeBaseFunctorList(parameters)
        for baseFunctor in baseFunctorList:
            if debugMode:
                print(baseFunctor[0].ToString())
            prevDiscripancy = sys.float_info.max
            bestDiscripancy = sys.float_info.max
            bestRegression = []
            bestKoefficients = []
            
            for regression in regressionList:
                if fastMode:
                    startRegressionTime = timeit.default_timer()
                for power in range(0, 20 + 1):
                    isError = False;
                    if fastMode:
                        currRegressionTime = timeit.default_timer()
                        if(currRegressionTime - startRegressionTime > 5):
                            break

                    currentRegression = regression.GetRegression(baseFunctor, power)
                    try:
                        currentKoefficients = approximation.CalcKoefficients(currentRegression)
                    except OverflowError:
                        isError= True
                        break

                    if len(currentKoefficients) == 0:
                        isError = True;
                        
                    currentDiscripancy = approximation.CalcDiscripancy(currentKoefficients, currentRegression)
                    if isError and debugMode:
                        GuessApproximation.__Warning(parameters, results, power, currentRegression, currentKoefficients, currentDiscripancy)
                        continue;

                    #if(not GuessApproximation.__CheckNonNegative(currentKoefficients, currentRegression, max(parameters)[0])):
                    #    continue
                    currentKoefficients = GuessApproximation.__RoundKoefficients(currentKoefficients)
                    
                    
                    currentDiscripancy = approximation.CalcDiscripancy(currentKoefficients, currentRegression)
                    
                    if debugMode:
                        print(f"currentDiscripancy: {currentDiscripancy}", end='')
                        if currentDiscripancy < prevDiscripancy:
                            print(" ▼")
                        else:
                            print(" ▲")

                    if(currentDiscripancy < totalBestDiscripancy):
                        totalBestDiscripancy = currentDiscripancy
                        totalBestRegression = currentRegression
                        totalBestKoefficients = currentKoefficients

                    for j in range(len(totalBestKoefficients) - 1, -1, -1):
                        if(totalBestKoefficients[j] == 0):
                            totalBestKoefficients.pop(j)
                            totalBestRegression.pop(j)
                
                    if(currentDiscripancy < bestDiscripancy):
                        bestDiscripancy = currentDiscripancy
                        bestRegression = currentRegression
                        bestKoefficients = currentKoefficients

                    for j in range(len(bestKoefficients) - 1, -1, -1):
                        if(bestKoefficients[j] == 0):
                            bestKoefficients.pop(j)
                            bestRegression.pop(j)

                    prevDiscripancy = currentDiscripancy

                    if(currentDiscripancy == 0):
                        break;
                    if not fullBustMode and totalBestDiscripancy <= GuessApproximation.goodDiscripancy_:
                        return totalBestKoefficients, totalBestRegression, totalBestDiscripancy;
                
            if debugMode:
                print(f"\nbaseFunctor: {baseFunctor[0].ToString()}")
                print(f"\tbestDiscripancy: {bestDiscripancy}")
                print(f"\tbestRegression: {bestRegression}")
                print(f"\tbestKoefficients: {bestKoefficients}")       
            
            
        return totalBestKoefficients, totalBestRegression, totalBestDiscripancy

    

   
    def __RoundKoefficients(koefficients: list):
        """
        Округляет только те коэффициенты которые очень близки к целым числам
        """

        ndigits = 0#округление до целого числа

        for i in range(len(koefficients)):
            koeff = koefficients[i];
            roundKoeff = round(koeff, ndigits).normalize()

            if math.isclose(koefficients[i], roundKoeff):
                koefficients[i] = roundKoeff
                #print(f"{koeff}->{roundKoeff}")

        return koefficients;

    def __MakeBaseFunctorList(parameters):
        """
        Инициализирует список базовых зависимостей
        """
        baseFunctors = []
        hasZero = False
        for row in parameters:
            if row.__contains__(0):
                hasZero = True
                break


        parametersWidth = len(parameters[0])

        functorList = []
        for i in range(parametersWidth):
            functorList.append(X(i))
        baseFunctors.append(functorList)
        
        if not hasZero:
            functorList = []
            for i in range(parametersWidth):
                functorList.append(Ceil(Log2(X(i))))
            baseFunctors.append(functorList)

        functorList = []
        for i in range(parametersWidth):
            functorList.append(Ceil(Exp(X(i))))
        baseFunctors.append(functorList)


        return baseFunctors

    def __SimplifyParameters(parameters):
        """
        Удапляет из parameters одинаковые столбцы
        """
        for i in range(len(parameters[0]) - 1, 0, -1):
            bNotFullRepeat = False
            val = parameters[0][i]
            for j in range(1, len(parameters)):
                if(val != parameters[j][i]):
                    bNotFullRepeat = True
                    break
            if(not bNotFullRepeat):
                for j in range(0, len(parameters)):
                    parameters[j].pop(i)
        return parameters

    def __CheckNonNegative(currentKoefficients, currentRegression, maxValue):
        """
        DEPRICATED
        """
        conformity = currentRegression.GetConformity()
        for i in range(0, len(conformity)):
            param = dict()
            
            for j in range(0, len(conformity)):
                if(i != j):
                    param[conformity[j]] = 1
                else:
                    param[conformity[j]] = maxValue
            
            if(FunctorListMethods.CalculateDependence(currentKoefficients, currentRegression, param) < 0):
                return False
 
        return True;

    def __Warning(parameters, results, power, currentRegression, currentKoefficients, currentDiscripancy):
        print("WARNING!!!\a")
        print(f"parameters: {parameters}")
        print(f"results: {results}")
        print(f"power: {power}")
        print(f"currentRegression: {currentRegression}")
        print(f"currentKoefficients: {currentKoefficients}")
        print(f"currentDiscripancy: {currentDiscripancy}")              