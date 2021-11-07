from abc import abstractmethod

class BaseFunctor_:
    @abstractmethod
    def GetConformity(self) -> list:
        raise NotImplementedError;

    @abstractmethod
    def __call__(self, data : list):
        raise NotImplementedError;
    
    @abstractmethod
    def __str__(self) -> str:
        return self.ToString(bLatex=False);

    @abstractmethod
    def ToString(self, bLatex=False) -> str:
        raise NotImplementedError;

    @abstractmethod
    def __eq__(self, other) -> bool: 
        raise NotImplementedError;
