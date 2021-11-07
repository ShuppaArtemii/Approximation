from decimal import Decimal
from Approximation.Approximation import Approximation

def GetStringDependence(koefficients, functorsList):
    string = "y = "
    if(len(koefficients) == 0 or len(functorsList) == 0):
        string += '?'
    else:
        string += str(koefficients[0])
        if(functorsList[0].ToString() != ""):
            string += "*" + functorsList[0].ToString()

        for i in range(1, len(functorsList)):
            if(koefficients[i] > 0):
                string+= "+"
            string += str(koefficients[i])
            if(functorsList[i].ToString() != ""):
                string += "*" + functorsList[i].ToString()
    return string

def GetStringDiscripancy(discripancy):
    return "Discripancy: " + str(discripancy)

def GetStringInfo(koefficients, functorsList, discripancy):
    string = GetStringDependence(koefficients, functorsList)
    string += "\n" + GetStringDiscripancy(discripancy)
    return string

def CalculateDependence(koefficients, functorsList, params):
    if(len(koefficients) != len(functorsList)):
        raise Exception("len(koefficients) != len(functorsList)")

    #result = 0
    #for i in range(len(koefficients)):
    #    sum = Decimal(0)
    #    if(len(functorsList[i].GetConformity()) == 0):
    #        sum = Decimal(1)
    #    else:
    #        for j in range(0, len(functorsList[i].GetConformity())):
    #            sum += Decimal(functorsList[i](params))
    #    result += koefficients[i] * sum
    #    print(f"{result}")

    result = 0; 
    for funcIdx in range(len(functorsList)):
        result += koefficients[funcIdx] * Decimal(functorsList[funcIdx](params));
        #print(result)
        
    return result;
