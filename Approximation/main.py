from Approximation.GuessApproximation import GuessApproximation
from Approximation.OutputData import OutputData
from Schedule.Schedule import Schedule
import requests
import json

class Program:
    def __init__(self, debugMode=False):
        self.debugMode = debugMode
    
    def ProcessWidthAndHeight(self, dimentions, iterations, processors, ticks, fastMode=True):
        parameters = self.__MergeParameters(dimentions, iterations)

        width_koeff, width_func, width_disc = GuessApproximation.Analyse(parameters, processors, fastMode, debugMode=self.debugMode)
        
        #schedule = Schedule(width_koeff, width_func, parameters, processors)
        #if schedule.CanShow():
        #    schedule.Show();
        
        height_koeff, height_func, height_disc = GuessApproximation.Analyse(parameters, ticks, fastMode, debugMode=self.debugMode)
        #schedule = Schedule(height_koeff, height_func, parameters, ticks)
        #if schedule.CanShow():
        #    schedule.Show();

        ouputData = OutputData(width_koeff, width_func, height_koeff, height_func)
        return ouputData

    def Start(self):
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms')
        algorithms = response.json()['data']

        for alg in algorithms:
            if self.__SkipAlg(alg):
                continue
            self.fastMode = self.__SetFastMode(alg);

            self.__PrintAlgTitle(alg)
            
            dimentions, iterations, processors, ticks = self.__GetAlgorithmData(alg)
            ouputData = self.ProcessWidthAndHeight(dimentions, iterations, processors, ticks, self.fastMode)
            
            print(json.dumps(ouputData.data, indent=4))

    def __SetFastMode(self, alg):
        return alg['id'] in ('3', '10', '13')

    def __SkipAlg(self, alg):
        return False;#not alg['id'] in ('', '3', '');

    def __PrintAlgTitle(self, alg):
        print(f"================================={alg['name']}(id: {alg['id']}", end='');
        if self.fastMode:
            print(", fastMode: Activated", end='');
        print(")==================================")

    def __GetAlgorithmData(self, alg):
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + alg['id'] + '/determinants/matrix')
        determinant = response.json()['data']
        
        parameters = determinant['X']

        #Разделяем на составляющие
        dimentions =  [row[:len(parameters[0])-1] for row in parameters]
        iterations = [row[len(parameters[0])-1] for row in parameters]

        processors = determinant['y']['processors']
        ticks = determinant['y']['ticks']

        self.PrintInfoAlgorithm(alg, parameters, processors, ticks)

        return dimentions, iterations, processors, ticks


    def __MergeParameters(self, dimentions, iterations):
        parameters = []
        for i in range(len(dimentions)):
            row = dimentions[i].copy()
            row.append(iterations[i])
            parameters.append(row)
        return parameters

    
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
