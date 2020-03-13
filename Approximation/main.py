from Approximation import GuessApproximation
from Schedule import Schedule
from Approximation import FunctorListMethods
import ctypes
import requests

def Process(title, parameters, results):
    koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, results, fullSearch=False);
        
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
    response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms');
    algorithms = response.json()['data'];
    nameList = [];
    idList = [];
    for alg in algorithms:
        idList.append(alg['id']);
        nameList.append(alg['name']);

    for i in range(0, len(idList)):
        response = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + idList[i] + '/determinants/matrix');
        determinant = response.json()['data'];
        parameters = determinant['X'];
        processors = determinant['y']['processors'];
        ticks = determinant['y']['ticks'];

        print(idList[i] + ") " + nameList[i]);
        print(parameters);
        print(processors);
        print(ticks);
        
        print("processors");
        Process(nameList[i] + " (processors/width)", parameters, processors);
        
        print("ticks");
        Process(nameList[i] + " (ticks/height)", parameters, ticks);
