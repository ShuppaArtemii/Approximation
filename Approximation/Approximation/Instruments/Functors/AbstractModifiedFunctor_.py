from Approximation.Instruments.Functors import BaseFunctor
from abc import ABC, abstractmethod

class AbstractModifiedFunctor_(BaseFunctor.BaseFunctor):
    def __init__(self, baseFunctor):
        super().__init__(baseFunctor, baseFunctor.conformity_ , baseFunctor.strFunction_);

    @abstractmethod
    def __call__(self, list):
        return super().__call__(list);

    def ToString(self):
        return super().ToString();

