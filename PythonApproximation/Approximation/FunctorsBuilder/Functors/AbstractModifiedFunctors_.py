from FunctorsBuilder.BaseFunctors import BaseFunctors
from abc import ABC, abstractmethod

class AbstractModifiedFunctors_(BaseFunctors.BaseFunctors):
    def __init__(self, baseFunctors):
        super().__init__(baseFunctors.functions_, baseFunctors.conformities_ , baseFunctors.strFunctions_);

    @abstractmethod
    def __call__(self, list):
        return super().__call__(list);

    def ToString(self):
        return super().ToString();
