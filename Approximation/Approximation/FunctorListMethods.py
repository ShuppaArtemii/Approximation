
def CalculateDependence(koefficients, functorsList, params):
    if(len(koefficients) != len(functorsList)):
        raise Exception("len(koefficients) != len(functorsList)")

    result = 0; 
    for funcIdx in range(len(functorsList)):
        result += koefficients[funcIdx] * float(functorsList[funcIdx](params));
        
    return result;
