
if __name__ == '__main__':
    
    algorithms = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms').json()['data'];
    for algId in range(1, len(algorithms) + 1):
        print(str(algId) + ") " + algorithms[algId-1]['name']);

        jsonRequest = requests.get('https://qserverr.herokuapp.com/api/v2/algorithms/' + str(algId) + '/determinants/matrix').json();
        parameters = jsonRequest['data']['X'];
        if(len(parameters) < 2):
            print("Not found");
            print();
            continue;
        processors = jsonRequest['data']['y']['processors'];
        ticks = jsonRequest['data']['y']['ticks'];
        
        DeleteConstantColomns(parameters);

        functions, koefficients, discripancy = StartApproximation(parameters, ticks);
        print("Ticks");
        print("Koefficients: ", koefficients);
        print("Discripancy: ", discripancy);
        print();
        if(len(koefficients) < 3):
            Chart3D.Draw(koefficients, functions, -100, 100, 1);
        else: print("multidimensional graphics don't support yet")

        functions, koefficients, discripancy = StartApproximation(parameters, processors);
        print("Processors");
        print("Koefficients: ", koefficients);
        print("Discripancy: ", discripancy);
        print();
        if(len(koefficients) < 3):
            Chart3D.Draw(koefficients, functions, -100, 100, 1);
        else: print("multidimensional graphics don't support yet")

