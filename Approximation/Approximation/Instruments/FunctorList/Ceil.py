from Approximation.Instruments.FunctorList.AbstractFunctorList import AbstractFunctorList_

class Ceil(AbstractFunctorList_):
    def __init__(self, functorList : AbstractFunctorList_, bCeil=True):
        super().__init__(functorList)
        self.functorList = functorList;
        self.bCeil = bCeil;

    def __call__(self, data : list):
        res = self.functorList(data);
        if (self.bCeil):
            res = math.ceil(res);
        return res;

    def SetCeil(self, bCeil):
        self.bCeil = bCeil;

    def __str__(self):
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False):
        return "ceil(" + self.functorList.ToString(bLatex) + ")";