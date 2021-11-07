from Approximation.Instruments.FunctorList.AbstractFunctorList import AbstractFunctorList_
from decimal import Decimal

class Multiplication(AbstractFunctorList_):
    def __init__(self, functorList : list):
        super().__init__(functorList);
        
    def __call__(self, data : list):
        if(len(self) == 0):
            raise Exception;
        
        mult = Decimal(1);
        for functor in self:
             mult *= Decimal(functor(data));
        return mult;
    
    def __str__(self):
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False):
        string = "";
        if(len(self) != 0):
            string += self[0].ToString(bLatex);
        for i in range(1, len(self)):
            string += "*" + self[i].ToString(bLatex);
        return string;
    
   
    