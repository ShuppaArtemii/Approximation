from Approximation import GuessApproximation
from Schedule import Schedule
from Approximation import FunctorListMethods

import requests

def Process(parameters, results):
    koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, results, fullSearch=False);
        
    minPoint = min(parameters)[0]
    maxPoint = max(parameters)[0]
    if(minPoint == 0 and maxPoint == 0):
        minPoint = -1;
        maxPoint = 1;

    info = FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy);
    print(info);
    Schedule.Draw(koefficients, functorsList, parameters, results, minPoint, maxPoint, minPoint, maxPoint, info);

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
        Process(parameters, processors);
        
        print("ticks");
        Process(parameters, ticks);
