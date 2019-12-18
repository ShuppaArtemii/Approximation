from FunctorsBuilder.AbstractModifiedFunctors_ import AbstractModifiedFunctors_
import math

class PowerFunctors(AbstractModifiedFunctors_):
    def __init(self, baseFunctors, power = 1):
        super().__init__(baseFunctors);
        self.power_ = power;

    def SetPower(self, power):
        self.power_ = power;

    def __call__(self, list):
        for i in range(len(list)):
            list[i] = math.pow(list[i], self.power_);
        
        sum = 0;
        for i  in range(len(self.functions_)):
            sum += self.functions_[i](list);

        return sum;
    
    def ToString(self):
        string = self.strFunctions_[0] + "^" + str(self.power_);
        
        for i in range(1, len(self.strFunctions_)):
            string += " + " + self.strFunctions_[i] + "^" + str(self.power_);

        return string;

