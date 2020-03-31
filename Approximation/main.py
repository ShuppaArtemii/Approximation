from Approximation.GuessApproximation import GuessApproximation
from Approximation.OutputData import OutputData
from Schedule import Schedule
from Approximation import FunctorListMethods
import ctypes
import requests
import json



from Approximation.Instruments.Regressions import PowerMultiplyRegression
from Approximation.Instruments.Functors import X, Log2, Ceil

def CalcAndDraw(parameters, results, title=""):
    koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, results, fullSearch=False);
    Draw(koefficients, functorsList, parameters, results, title)    
    

def Draw(koefficients, functorsList, parameters, results, title=""):
    minPoint = min(parameters)[0]
    maxPoint = max(parameters)[0]
    if(minPoint == 0 and maxPoint == 0):
        minPoint = 0;
        maxPoint = 1;

    info = FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy);
    print(info);
    
    try:
        Schedule.Draw(koefficients, functorsList, parameters, results, minPoint, maxPoint, minPoint, maxPoint, title + '\n' +
                  FunctorListMethods.GetStringDiscripancy(discripancy),
                  FunctorListMethods.GetStringDependence(koefficients, functorsList));
    except ValueError as e:
        text = '';
        if hasattr(e, 'message'):
            text = e.message;
        else:
            text = str(e);
        ctypes.windll.user32.MessageBoxW(0, text, 'Error', 0);

if __name__ == '__main__':
    #functorsList = PowerMultiplyRegression.PowerMultiplyRegression.GetRegression([X.X([0]), X.X([1])], 2);
    #Schedule.Draw([0, 0, 0, 0, 1, 0], functorsList, [], [], 0, 10, 0, 10, "Default algorithm\n", str(functorsList[4]));
    
    response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms');
    algorithms = response.json()['data'];
    nameList = [];
    idList = [];
    for alg in algorithms:
        idList.append(alg['id']);
        nameList.append(alg['name']);
    for i in range(8, len(idList)):
        print(idList[i] + ") " + nameList[i]);
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + idList[i] + '/determinants/matrix');
        determinant = response.json()['data'];
        parameters = determinant['X'];
        processors = determinant['y']['processors'];
        ticks = determinant['y']['ticks'];
        
        print("processors: ");
        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, processors, fullSearch=False, bDebug=False);
        outputData  = OutputData(koefficients, functorsList);
        print(json.dumps(outputData.data));
        Draw(koefficients, functorsList, parameters, processors, nameList[i] + " (proc.)\n");

        print("\nticks: ");
        koefficients, functorsList, discripancy = GuessApproximation.Analyse(parameters, ticks, fullSearch=False, bDebug=False);
        outputData  = OutputData(koefficients, functorsList);
        print(json.dumps(outputData.data));
        Draw(koefficients, functorsList, parameters, ticks, nameList[i] + " (ticks)\n");

        #input();