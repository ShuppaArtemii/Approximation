from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_

class X(BaseFunctor_):
    def __init__(self, conformity : list):
        super().__init__(None, conformity);

    def GetConformity(self):
        return self.conformity_;
    
    def __call__(self, data):
        return data[self.conformity_[0]];#TODO: [0] because data builds in special function using self.conformity_; not cool to send a full list of data each time

    def __str__(self):
        return self.ToString(bLatex=False);

    def ToString(self, bLatex=False):
        string = "x";
        if bLatex:
            string += "_";
        string += str(self.conformity_[0] + 1);
        return string;