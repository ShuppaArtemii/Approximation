from abc import ABC, abstractmethod

class BaseFunctors:
    def __init__(self, functions, conformities, strFunctions):
        self.functions_ = functions;
        self.conformities_ = conformities;
        self.strFunctions_ = strFunctions;

    @abstractmethod
    def __call__(self, list):
        sum = 0;
        for i in range(len(self.functions_)):
            sum += self.functions_[i](self.GetFunctionParameters_(self.conformities_[i], list));
        
        return sum;

    def ToString(self):
        string = self.strFunctions_[0];
        for i in range(1, len(self.strFunctions_)):
            string += " + " + self.strFunctions_[i];

        return string;

    def GetFunctionParameters_(self, conformity, list):
        parameters = [];
        for i in range(len(conformity)):
            parameters.append(list[conformity[i]]);

        return parameters;

