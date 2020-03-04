from Approximation import GuessApproximation
from Schedule import Schedule
from Approximation import FunctorListMethods

import requests

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
        koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, processors, fullSearch=False);
        info = FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy);
        print(info);
        Schedule.Draw(koefficients, functorsList, 1, 10, 1, 10, info);

        print("ticks");
        koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, ticks, fullSearch=False);
        info = FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy);
        print(info);
        Schedule.Draw(koefficients, functorsList, 1, 10, 1, 10, info);
