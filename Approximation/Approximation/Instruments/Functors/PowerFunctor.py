from Approximation.Instruments.Functors import AbstractModifiedFunctor_
import math

class PowerFunctor(AbstractModifiedFunctor_.AbstractModifiedFunctor_):
    def __init(self, baseFunctor, power = 1):
        super().__init__(baseFunctor);
        self.power_ = power;

    def SetPower(self, power):
        self.power_ = power;

    def __call__(self, list):
        for i in range(len(list)):
            list[i] = math.pow(list[i], self.power_);
        
        return super().__call__(list);
    
    def ToString(self):
        return self.strFunction_ + "^" + str(self.power_);

    def __eq__(self, other):
        return super().__eq__(other) and self.power_ == other.power_;