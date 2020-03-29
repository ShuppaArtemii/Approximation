from abc import abstractmethod

class AbstractFunctorList_(list):
    def __init__(self, functorList : list):
        super().__init__(functorList);

    @abstractmethod
    def __call__(self, data : list):
        raise NotImplementedError;

    def GetConformity(self):
        result = [];
        for functor in self:
            conformityList = functor.GetConformity();
            for conformity in conformityList:
                if(not conformity in result):
                    result.append(conformity);
        return result;

    def GetFunctionParameters_(self, conformityList : list, data : list):
        parameters = [];
        if(len(conformityList) == len(data)):
            parameters = data.copy();
        else:
            for conformity in conformityList:
                parameters.append(data[conformity]);
        return parameters;

    def __str__(self):
        return self.ToString(bLatex=False);
    
    @abstractmethod
    def ToString(self, bLatex=False):
        raise NotImplementedError;