from abc import abstractmethod

class BaseFunctor_:
    def __init__(self, childFunctor, conformity : list):
        self.childFunctor_ = childFunctor;
        self.conformity_ = conformity;

    @abstractmethod
    def GetConformity(self):
        return self.conformity_;

    @abstractmethod
    def __call__(self, data : list):
        raise NotImplementedError;
    
    @abstractmethod
    def __str__(self):
        return self.ToString(bLatex=False);

    @abstractmethod
    def ToString(self, bLatex=False):
        raise NotImplementedError;

    def __eq__(self, other): 
        return self.childFunctor_ == other.childFunctor_ and \
            self.conformity_ == other.conformity_ and \
            self.strFunction_ == other.strFunction_;
