
class OutputData:
    def __init__(self, koefficients, functorsList):
        self.data = {};
        self.data['data'] = {};

        self.data['data']['coef'] = [];
        for i in range(len(koefficients)):
            self.data['data']['coef'].append(koefficients[i]);

        constName = "1";
        self.data['data']['names'] = [];
        for i in range(len(functorsList)):
            if len(functorsList[i].GetConformity()) == 0 and constName not in self.data['data']['names']:
                self.data['data']['names'].append(constName);

            for j in range(len(functorsList[i].GetConformity())):
                name = str(functorsList[i]);
                if name not in self.data['data']['names']:
                    self.data['data']['names'].append(name);
    
        self.data['data']['json'] = [];
        for i in range(len(koefficients)):
            jsonElem = {};
            jsonElem['coef'] = koefficients[i];
            jsonElem['variables'] = [];
            for j in range(len(functorsList[i])):
                if(len(functorsList[i].GetConformity()) != 0):
                    variable = {
                    'index': functorsList[i].GetConformity()[j] + 1,
                    'pow': functorsList[i][j].power_
                    }
                    jsonElem['variables'].append(variable);
            

            self.data['data']['json'].append(jsonElem);
    
        self.data['data']['latex'] = self.GetLatexPowerString_(koefficients, functorsList);

    def GetFormatNumber_(self, number):
        return str(number);#format(number).rstrip('0').rstrip('.');

    def GetLatexPowerString_(self, koefficients, functorsList):
        latexString = "";
        for i in range(len(koefficients)):
            latexString += self.GetFormatNumber_(koefficients[i]) + functorsList[i].ToString(bLatex=True);
            
            if(not i == len(koefficients) - 1):
                latexString += " + ";
        
        return latexString;
