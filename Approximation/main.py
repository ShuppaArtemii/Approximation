from Approximation.GuessApproximation import GuessApproximation
from Approximation.OutputData import OutputData
from Schedule.Schedule import Schedule
from Approximation import FunctorListMethods
import ctypes
import requests
import json
from pathlib import Path 

if __name__ == '__main__':
    response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms');
    algorithms = response.json()['data'];
    
    nameList = [];
    idList = [];
    for alg in algorithms:
        idList.append(alg['id']);
        nameList.append(alg['name']);
    
    for i in range(0, len(idList)):
        print(idList[i] + ") " + nameList[i]);
        
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + idList[i] + '/determinants/matrix');
        determinant = response.json()['data'];
        parameters = determinant['X'];
        processors = determinant['y']['processors'];
        ticks = determinant['y']['ticks'];
        
        #Path("Graphs/" + idList[i] + ". " + nameList[i]).mkdir(parents=True, exist_ok=True);

        #==========================================Processors========================================================================
        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, processors, fullSearch=False, bDebug=False);
        schedule = Schedule(koefficients, functorsList, parameters, processors);
        outputData  = OutputData(koefficients, functorsList, schedule);

        #with open("Graphs/" + idList[i] + ". " + nameList[i] + "/Processors.json", 'w', encoding='utf-8') as f:
        #    json.dump(outputData.data, f, ensure_ascii=False, indent=4);


        #==========================================Ticks========================================================================
        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, ticks, fullSearch=False, bDebug=False);
        schedule = Schedule(koefficients, functorsList, parameters, ticks);
        outputData  = OutputData(koefficients, functorsList, schedule);
        
        #with open("Graphs/" + idList[i] + ". " + nameList[i] + "/Ticks.json", 'w', encoding='utf-8') as f:
        #    json.dump(outputData.data, f, ensure_ascii=False, indent=4);

        
        