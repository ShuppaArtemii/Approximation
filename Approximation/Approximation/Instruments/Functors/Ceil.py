from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
import math

class Ceil(BaseFunctor_):
    def __init__(self, childFunctor, bCeil : bool = True):
        super().__init__(childFunctor, None);
        self.bCeil_ = bCeil;
        
        
    def GetConformity(self):
        return self.childFunctor_.GetConformity();
    
    def SetCeil(self, bValue : bool):
        self.bCeil = bValue;

    def __call__(self, data : list):
        result = self.childFunctor_(data);
        
        if(self.bCeil_):
            return math.ceil(result);
        else: return result;

    def __str__(self):
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False):
        return self.childFunctor_.ToString(bLatex);
