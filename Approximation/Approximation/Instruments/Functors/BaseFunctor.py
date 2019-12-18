from abc import ABC, abstractmethod

class BaseFunctor:
    def __init__(self, function, conformity : list, strFunction : str):
        self.function_ = function;
        self.conformity_ = conformity;
        self.strFunction_ = strFunction;

    @abstractmethod
    def __call__(self, list):
        return self.function_(list);

    def ToString(self):
        return self.strFunction_;

    def __eq__(self, other): 
        return self.function_ == other.function_ and \
            self.conformity_ == other.conformity_ and \
            self.strFunction_ == other.strFunction_;
