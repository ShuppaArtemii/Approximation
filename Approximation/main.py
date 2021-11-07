from Approximation.GuessApproximation import GuessApproximation
from Approximation.OutputData import OutputData
from Schedule.Schedule import Schedule
from Approximation import FunctorListMethods
import ctypes
import requests
import json
from pathlib import Path 
import math
from decimal import Decimal

from Approximation.Approximation import Approximation
from Approximation.Instruments.Regressions.PowerMultiplyRegression import PowerMultiplyRegression

class Program:
    def __init__(self, debugMode=False):
        self.debugMode = debugMode

    def Start(self):
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms')
        algorithms = response.json()['data']

        for alg in algorithms:
            if self.__SkipAlg(alg):
                continue
            self.fastMode = self.__SetFastMode(alg);

            self.__PrintAlgTitle(alg)
            parameters, processors, ticks = self.__GetAlgorithmData(alg)
            
            print(f"---------------------------------------------------------Processors-----------------------------------------------------")
            self.__GuessApproximation(parameters, processors, self.fastMode)
            print(f"---------------------------------------------------------Ticks-----------------------------------------------------")
            self.__GuessApproximation(parameters, ticks, self.fastMode)


    def __SetFastMode(self, alg):
        return alg['id'] in ('3', '10', '12', '13')

    def __SkipAlg(self, alg):
        return False;
    
    def __PrintAlgTitle(self, alg):
        print(f"================================={alg['name']}(id: {alg['id']}", end='');
        if self.fastMode:
            print(", fastMode: Activated", end='');
        print(")==================================")

    def __GetAlgorithmData(self, alg):
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + alg['id'] + '/determinants/matrix')
        determinant = response.json()['data']
        parameters = determinant['X'] 
        processors = determinant['y']['processors']
        ticks = determinant['y']['ticks']

        self.PrintInfoAlgorithm(alg, parameters, processors, ticks)

        return parameters, processors, ticks
    
    def __GuessApproximation(self, parameters, results, fastSearch, drawShedule=True):

        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, results, fastMode=fastSearch, debugMode=self.debugMode)
        
        schedule = Schedule(koefficients, functorsList, parameters, results)
        outputData = OutputData(koefficients, functorsList, schedule)
       
        koeff = outputData.data['data']['coef']
        functions = outputData.data['data']['json']

        
        print(f"\tkoefficients: {koeff}") 
        print(f"\tfunctorsList: {functions}")
        print(f"\tdiscripancy: {discripancy}")

        if drawShedule:
            schedule.Show();
    
    def PrintInfoAlgorithm(self, alg, parameters, processors, ticks):
        if self.debugMode:
            print("parameters")
            print(f"{parameters}")
    
            print("processors")
            print(f"{processors}")

            print("ticks")
            print(f"{ticks}")




if __name__ == '__main__':

    program = Program()
    program.Start()
