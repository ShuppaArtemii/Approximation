from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
import math

class Log2(BaseFunctor_):
    def __init__(self, childFunctor):
        super().__init__(childFunctor, None);
        
    def GetConformity(self):
        return self.childFunctor_.GetConformity();

    def __call__(self, data : list):
        result = self.childFunctor_(data);
        return math.log2(result);

    def __str__(self):
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False):
        return "log2(" + self.childFunctor_.ToString(bLatex) + ")";
    
    def __eq__(self, other): 
        return super().__eq__(other) and childFunctor_ == other.childFunctor_;