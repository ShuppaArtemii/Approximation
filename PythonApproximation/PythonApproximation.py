import sys
import copy
import math
import Chart3D
import requests
import Approximation as Approx;
from abc import ABC, abstractmethod

#Базовая функция - принимает список аргументов численного типа и возвращает одно единственное численное значение
def Return1(list):
	return 1;

def ReturnX(list):
	return list[0];

def ReturnLog2X(list):
    return math.log2(list[0]);

class FunctionWithConformity:
    """
    Обертка над базовой функцией, хранящая ссылку на эту функцию и список параметров "соответствий" для ее агрументов
    """
    def __init__(self, function, conformity):
        self.function = function;
        self.conformity = conformity;

    @abstractmethod
    def __call__(self, list):
       return self.function(list);

#Модифицированные функторы
class PowerFunction(FunctionWithConformity):
    def __init__(self, function, conformity):
        super().__init__(function, conformity);

    def SetPower(self, power):
        self.power = power;

    def __call__(self, list):
        for i in range(len(list)):
            list[i] = math.pow(list[i], self.power);
        return self.function(list);

#возвращает последовательность функторов в виде степенной последовательности
def GetSequencePowerFunction(baseFunction, startPower, stopPower):
    sequence = [];
    for power in range(startPower, stopPower):
        for funcIdx in range(len(baseFunction)):
            powerFunction = PowerFunction(baseFunction[funcIdx].function, baseFunction[funcIdx].conformity);
            powerFunction.SetPower(power);
            sequence.append(powerFunction);
    return sequence;

#возвращает последовательность функторов соответсвующей степенному многочлену
def GetPowerPolynom(functionWithConformity, power):
    polynom = [];
    polynom.append(FunctionWithConformity(Return1, []));
    polynom.extend(GetSequencePowerFunction(functionWithConformity, 1, power + 1))
    return polynom;


def StartApproximation(parameters, results):
    approximation = Approx.Approximation(parameters, results);
    
    bestFunction = [];
    bestKoefficients = [];
    bestDiscripancy = sys.float_info.max;
    
    #проверка для степенного многочлена
    baseFunc = [];
    for i in range(0, len(parameters[0])):#обход по столбцам (для каждой свободной переменной)
        funcReturn = FunctionWithConformity(ReturnX, [0]);
        funcReturn.conformity = [i];
        baseFunc.append(funcReturn);
        
    bestFunction = GetPowerPolynom(baseFunc, 20);
    bestKoefficients = approximation.New_CalcKoefficients(bestFunction);
    bestDiscripancy = approximation.New_CalcDiscripancy(bestKoefficients, bestFunction);
    
    if bestDiscripancy != 0:
        #проверка для многочлена из логарифмов 
        baseFunc = [];
        for i in range(0, len(parameters[0])):#обход по столбцам (для каждой свободной переменной)
            funcReturn = FunctionWithConformity(ReturnLog2X, [0]);
            funcReturn.conformity = [i];
            baseFunc.append(funcReturn);
            
        function = GetPowerPolynom(baseFunc, 20);
        koefficients = approximation.New_CalcKoefficients(bestFunction);
        discripancy = approximation.New_CalcDiscripancy(bestKoefficients, bestFunction);

        if(discripancy < bestDiscripancy):
            bestFunction = functions;
            bestKoefficients = koefficients;
            bestDiscripancy = discripancy;
    
    for i in range(len(bestKoefficients) - 1, 0, -1):
        if(bestKoefficients[i] != 0):
            break;
        else:
            bestKoefficients.pop(i);
            bestFunction.pop(i);
        

    return bestFunction, bestKoefficients, bestDiscripancy;

def DeleteConstantColomns(parameters):
    for j in range(1, len(parameters[0])):
        bRepeat = True;
        for i in range(len(parameters)):
            repeatedColomn = -1;
            if(parameters[i][j] != parameters[0][j]):
                bRepeat = False;
                break;
        if(bRepeat):
            for k in range(len(parameters)):
                parameters[k].pop(j);
        

if __name__ == '__main__':
    
    algorithms = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms').json()['data'];
    for algId in range(1, len(algorithms) + 1):
        print(str(algId) + ") " + algorithms[algId-1]['name']);

        #Для каждого алгоритма на сайте:
        #1) считываем необходимые данные
        jsonRequest = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + str(algId) + '/determinants/matrix').json();
        parameters = jsonRequest['data']['X'];
        if(len(parameters) < 2):
            print("Not found");
            print();
            continue;
        processors = jsonRequest['data']['y']['processors'];
        ticks = jsonRequest['data']['y']['ticks'];
        
        DeleteConstantColomns(parameters);

        #2)инициализируем их в объекте approximation
        functions, koefficients, discripancy = StartApproximation(parameters, ticks);
        print("Ticks");
        print("Koefficients: ", koefficients);
        print("Discripancy: ", discripancy);
        print();
        if(len(koefficients) < 3):
            Chart3D.Draw(koefficients, functions);
        else: print("multidimensional graphics don't support yet")

        functions, koefficients, discripancy = StartApproximation(parameters, processors);
        print("Processors");
        print("Koefficients: ", koefficients);
        print("Discripancy: ", discripancy);
        print();
        if(len(koefficients) < 3):
            Chart3D.Draw(koefficients, functions);
        else: print("multidimensional graphics don't support yet")
