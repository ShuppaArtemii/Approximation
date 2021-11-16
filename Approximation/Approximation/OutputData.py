from io import BytesIO
import base64

class OutputData:
    def __init__(self, width_koefficients, width_functorsList, height_koefficients, height_functorsList):
        self.data = {};
        self.data['data_width']  = self.__GetDependenceString( width_koefficients,  width_functorsList, bLatex=False)
        self.data['data_height'] = self.__GetDependenceString(height_koefficients, height_functorsList, bLatex=False)

    
    #def __init__(self, koefficients, functorsList, schedule):
    #"""DERPICATED"""
    #
    #    self.data = {};
    #    self.data['data'] = {};

    #    self.data['data']['coef'] = [];
    #    for i in range(len(koefficients)):
    #        self.data['data']['coef'].append(koefficients[i]);

    #    constName = "1";
    #    self.data['data']['names'] = [];
    #    for i in range(len(functorsList)):
    #        if len(functorsList[i].GetConformity()) == 0 and constName not in self.data['data']['names']:
    #            self.data['data']['names'].append(constName);

    #        for j in range(len(functorsList[i].GetConformity())):
    #            name = str(functorsList[i]);
    #            if name not in self.data['data']['names']:
    #                self.data['data']['names'].append(name);
    
    #    self.data['data']['json'] = [];
    #    for i in range(len(koefficients)):
    #        jsonElem = {};
    #        jsonElem['coef'] = koefficients[i];
    #        jsonElem['variables'] = [];
    #        for j in range(len(functorsList[i])):
    #            if(len(functorsList[i].GetConformity()) != 0):
    #                variable = {
    #                'index': functorsList[i].GetConformity()[j] + 1,
    #                'pow': functorsList[i][j].power_
    #                }
    #                jsonElem['variables'].append(variable);
            

    #        self.data['data']['json'].append(jsonElem);
    
    #    self.data['data']['latex'] = self.__GetLatexPowerString(koefficients, functorsList);
        
    #    if(schedule != None and schedule.CanShow()):
    #        rawBytes = BytesIO();
    #        schedule.SaveToBuffer(rawBytes, 'png');

    #        bytesValue = base64.b64encode(rawBytes.getbuffer());
    #        jsonValue = bytesValue.decode('UTF-8').replace("'", '"');
    #        self.data['data']['img'] = "data:image/png;base64," + jsonValue;
    #    else:
    #        self.data['data']['img'] = "";
            

    def __GetFormatNumber(self, number):
        return str(number);

    def __GetTermString(self, koeff, function, bLatex=False):
        string = "";
        string += self.__GetFormatNumber(abs(koeff));
        fnStr = function.ToString(bLatex);
        if fnStr != "":
            string += "*" + fnStr;
        return string;

    def __GetDependenceString(self, koefficients, functorsList, bLatex=False):
        string = "";
        for i in range(len(koefficients)):
            string += self.__GetTermString(koefficients[i], functorsList[i], bLatex)
            if (i+1 < len(koefficients)):
                if (koefficients[i] >= 0):
                    string += " + ";
                else:
                    string += " - ";

        return string;
