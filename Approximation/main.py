from Approximation.GuessApproximation import GuessApproximation
from Approximation.OutputData import OutputData
from Schedule.Schedule import Schedule
from Approximation import FunctorListMethods
import ctypes
import requests
import json

from pathlib import Path
def MakeShedule(koefficients, functorsList, parameters, results, title="", subtitle="", legend=""):
    #set default arguments
    minX = minY = min(parameters)[0]
    maxX = maxY = max(parameters)[0]
    if(minX == 0 and maxX == 0):
        minX = minY = 0;
        maxX = maxY = 1;

    if(subtitle == ""): subtitle = FunctorListMethods.GetStringDiscripancy(discripancy);
    if(legend == ""): legend = FunctorListMethods.GetStringDependence(koefficients, functorsList);


    try:
        schedule = Schedule(koefficients, functorsList, parameters, results, minX, maxX, minY, maxY, title, subtitle, legend);
        return schedule;

    except ValueError as e:
        text = '';
        if hasattr(e, 'message'):
            text = e.message;
        else:
            text = str(e);
        ctypes.windll.user32.MessageBoxW(0, text, 'Error', 0);
    
    return None;

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
        
        Path("Graphs/" + idList[i] + ". " + nameList[i]).mkdir(parents=True, exist_ok=True);

        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, processors, fullSearch=False, bDebug=False);
        outputData  = OutputData(koefficients, functorsList);
        
        #with open("Approximation/" + idList[i] + ". " + nameList[i] + "/Processors.json", 'w', encoding='utf-8') as f:
        #    json.dump(outputData.data, f, ensure_ascii=False, indent=4)
        
        schedule = MakeShedule(koefficients, functorsList, parameters, processors, nameList[i] + " (proc.)");
        
        if(not schedule == None):
            #schedule.Save("Approximation/" + idList[i] + ". " + nameList[i] + "/Processors.png");
            schedule.Show();

        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, ticks, fullSearch=False, bDebug=False);
        outputData  = OutputData(koefficients, functorsList);
        
        with open("Graphs/" + idList[i] + ". " + nameList[i] + "/Ticks.json", 'w', encoding='utf-8') as f:
            json.dump(outputData.data, f, ensure_ascii=False, indent=4);

        schedule = MakeShedule(koefficients, functorsList, parameters, ticks, nameList[i] + " (ticks)");
        
        if(not schedule == None):
            #schedule.Save("Approximation/" + idList[i] + ". " + nameList[i] + "/Ticks.png");
            schedule.Show();
        
        
