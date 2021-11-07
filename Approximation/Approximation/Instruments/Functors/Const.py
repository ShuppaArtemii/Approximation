from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
from decimal import Decimal

class Const(BaseFunctor_):
    def GetConformity(self):
        return [];

    def __call__(self, data : list):
        return Decimal(1);

    def __str__(self) -> str:
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False) -> str:
        if(bLatex):
            return "";
        else:
            return "1";

    def __eq__(self, other) -> bool: 
        return other is Const;