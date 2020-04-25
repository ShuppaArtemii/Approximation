from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
import math

class Power(BaseFunctor_):
    def __init__(self, childFunctor, power = 1):
        super().__init__(childFunctor, childFunctor.conformity_);
        self.SetPower(power);

    def GetConformity(self):
        return self.childFunctor_.GetConformity();

    def SetPower(self, power):
        self.power_ = power;

    def __call__(self, data):
        result = self.childFunctor_(data);
        return math.pow(result, self.power_);

    def __str__(self):
        return self.ToString(bLatex=False);

    def ToString(self, bLatex=False):
        string = "";
        if(self.power_ != 0):
            string += self.childFunctor_.ToString(bLatex);
            if(self.power_ != 1):
                string += "^" + str(self.power_);
        return string;