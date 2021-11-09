from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
import math

class Power(BaseFunctor_):
    def __init__(self, internalFunctor, power):
        self.internalFunctor_ = internalFunctor;
        self.SetPower(power);

    def GetConformity(self):
        return self.internalFunctor_.GetConformity();

    def SetPower(self, power):
        self.power_ = power;

    def __call__(self, data):
        result = self.internalFunctor_(data);
        return result**self.power_;

    def __str__(self):
        return self.ToString(bLatex=False);

    def ToString(self, bLatex=False):
        string = "";
        if(self.power_ != 0):
            string += self.internalFunctor_.ToString(bLatex);
            if(self.power_ != 1):
                string += "^";
                if(bLatex):
                     string += "{" + str(self.power_) + "}";
                else:
                    string += str(self.power_);

        return string;

    def __eq__(self, other): 
        return \
            type(other) is Power and\
            self.power_ == other.power_ and\
            self.internalFunctor_ == other.internalFunctor_;