from io import BytesIO
import base64

class OutputData:
    def __init__(self, koefficients, functorsList, schedule):
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
    
        self.data['data']['latex'] = self.__GetLatexPowerString(koefficients, functorsList);
        
        if(schedule != None and schedule.CanShow()):
            rawBytes = BytesIO();
            schedule.SaveToBuffer(rawBytes, 'png');

            bytesValue = base64.b64encode(rawBytes.getbuffer());
            jsonValue = bytesValue.decode('UTF-8').replace("'", '"');
            self.data['data']['img'] = "data:image/png;base64," + jsonValue;
        else:
            self.data['data']['img'] = "";
            

    def __GetFormatNumber(self, number):
        return str(number);

    def __GetLatexPowerString(self, koefficients, functorsList):
        latexString = "";
        i = 0;
        while(i < len(koefficients) - 1):
            latexString += self.__GetFormatNumber(abs(koefficients[i])) + functorsList[i].ToString(bLatex=True);
            
            if(koefficients[i + 1] >= 0):
                latexString += " + ";
            else:
                latexString += " - ";
            i += 1;

        latexString += self.__GetFormatNumber(abs(koefficients[i])) + functorsList[i].ToString(bLatex=True);
        return latexString;
