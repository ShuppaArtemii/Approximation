from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_

class X(BaseFunctor_):
    def __init__(self, conformity: int):
        self.conformity_ = conformity;

    def GetConformity(self):
        return [self.conformity_];
    
    def __call__(self, data):
        return data[self.conformity_];

    def __str__(self):
        return self.ToString(bLatex=False);

    def ToString(self, bLatex=False):
        string = "x";
        if bLatex:
            string += "_{";
        string += str(self.conformity_ + 1);
        if bLatex:
            string += "}";
        return string;

    def __eq__(self, other):
        return type(other) is X and self.conformity_ == other.conformity_;