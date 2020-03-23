
class OutputData:
    def __init__(self, koefficients, functorsList):
        self.data = {};
        self.data['data'] = {};

        self.data['data']['coef'] = [];
        for i in range(len(koefficients)):
            self.data['data']['coef'].append(self.GetFormatNumber_(koefficients[i]));

        constName = "1";
        self.data['data']['names'] = [];
        for i in range(len(functorsList)):
            if len(functorsList[i].conformity_) == 0 and constName not in self.data['data']['names']:
                self.data['data']['names'].append(constName);

            for j in range(len(functorsList[i].conformity_)):
                name = functorsList[i].ToString();
                if name not in self.data['data']['names']:
                    self.data['data']['names'].append(name);
    
        self.data['data']['json'] = [];
        for i in range(len(koefficients)):
            jsonElem = {};
            jsonElem['coef'] = self.GetFormatNumber_(koefficients[i]);
            jsonElem['variables'] = [];
            for j in range(len(functorsList[i].conformity_)):
                variable = {
                    'index': functorsList[i].conformity_[j] + 1,
                    'pow': functorsList[i].power_
                }
                jsonElem['variables'].append(variable);
            self.data['data']['json'].append(jsonElem);
    
        self.data['data']['latex'] = self.GetLatexPowerString_(koefficients, functorsList);

    def GetFormatNumber_(self, number):
        return format(number).rstrip('0').rstrip('.');

    def GetLatexPowerString_(self, koefficients, functorsList):
        latexString = "";
        for i in range(len(koefficients)):
            latexString += self.GetFormatNumber_(koefficients[i]) + functorsList[i].strFunction_;
            if(not len(functorsList[i].conformity_) == 0):
                latexString += "_";
            for j in range(len(functorsList[i].conformity_)):
                latexString += str(functorsList[i].conformity_[j] + 1);
        
            if hasattr(functorsList[i], 'power_'):
                if(not functorsList[i].power_ == 1):
                    latexString += "^" + str(functorsList[i].power_);
            if(not i == len(koefficients) - 1):
                latexString += " + ";
        
        return latexString;