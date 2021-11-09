from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
import math

class Ceil(BaseFunctor_):
    def __init__(self, internalFunctor, IsActive : bool = True):
        self.internalFunctor_ = internalFunctor;
        self.IsActive_ = IsActive;
        
    def GetConformity(self):
        return self.internalFunctor_.GetConformity();
    
    def SetActive(self, bValue : bool):
        self.IsActive_ = bValue;

    def __call__(self, data : list):
        result = self.internalFunctor_(data);
        
        if(self.IsActive_):
            return math.ceil(result);
        else: return result;

    def __str__(self):
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False):
        return self.internalFunctor_.ToString(bLatex);

    def __eq__(self, other): 
        return \
            type(other) is Ceil and \
            IsActive_ == other.IsActive_ and \
            internalFunctor == other.internalFunctor;
