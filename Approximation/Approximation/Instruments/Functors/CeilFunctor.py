from Approximation.Instruments.Functors import AbstractModifiedFunctor_
import math

class CeilFunctor(AbstractModifiedFunctor_.AbstractModifiedFunctor_):
    def __init__(self, baseFunctor, bCeil : bool = True):
        super().__init__(baseFunctor);
        self.SetCeil(bCeil);

    def SetCeil(self, bValue : bool):
        self.bCeil = bValue;

    def __call__(self, list):
        value = super().__call__(list);
        
        if(self.bCeil):
            return math.ceil(value);
        else: return value;

