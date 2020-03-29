from Approximation.Instruments.Functors.BaseFunctor import BaseFunctor_

class Const(BaseFunctor_):
    def __init__(self):
        super().__init__(None, []);
    
    def __call__(self, data : list):
        return 1;

    def __str__(self):
        return self.ToString(bLatex=False);
    
    def ToString(self, bLatex=False):
        if(bLatex):
            return "";
        else:
            return "1";