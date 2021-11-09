from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_
from decimal import Decimal
from enum import Enum


class Const(BaseFunctor_):
    def GetConformity(self):
        return [];

    def __call__(self, data : list):
        return Decimal(1);

    def __str__(self) -> str:
        return self.ToString();
    
    def ToString(self, bLatex=False) -> str:
       return "";

    def __eq__(self, other) -> bool: 
        return type(other) is Const;