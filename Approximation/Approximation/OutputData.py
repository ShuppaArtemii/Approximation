
class OutputData:
    def __init__(self, width_koefficients, width_functorsList, height_koefficients, height_functorsList):
        self.data = {};
        self.data['data_width']  = self.__GetDependenceString( width_koefficients,  width_functorsList, bLatex=False)
        self.data['data_height'] = self.__GetDependenceString(height_koefficients, height_functorsList, bLatex=False)

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
