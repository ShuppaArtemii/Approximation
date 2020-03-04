
def GetStringDependence(koefficients, functorsList):
    string = "y = ";
    if(len(koefficients) == 0 or len(functorsList) == 0):
        string += '?';
    else:
        string += str(koefficients[0]);
        if(functorsList[0].ToString() != ""):
            string += "*" + functorsList[0].ToString();

        for i in range(1, len(functorsList)):
            string += " + " + str(koefficients[i]);
            if(functorsList[i].ToString() != ""):
                string += "*" + functorsList[i].ToString();
    return string;

def GetStringDiscripancy(discripancy):
    return "Discripancy: " + str(discripancy);

def GetStringInfo(koefficients, functorsList, discripancy):
    string = GetStringDependence(koefficients, functorsList);
    string += "\n" + GetStringDiscripancy(discripancy);
    return string;

def CalculateDependence(koefficients, functorsList, params):
    if(len(koefficients) != len(functorsList)):
        raise Exception("len(koefficients) != len(functorsList)");

    result = 0;
    for i in range(len(koefficients)):
        sum = 0;
        for j in range(0, len(functorsList[i].conformity_)):
            sum += functorsList[i]([ params[functorsList[i].conformity_[j]] ]);
        result += koefficients[i] * sum;
        
    return result;