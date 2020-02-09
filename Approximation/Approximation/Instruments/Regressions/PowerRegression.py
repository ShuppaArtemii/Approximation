from abc import ABC, abstractmethod
from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Sequences import PowerSequence
from Approximation.Instruments.Functions import *

class PowerRegression:
    def GetRegression(baseFunctor : list, power):
        regression = [];
        regression.append(BaseFunctor.BaseFunctor(Return1, [], ""));
        sequence = PowerSequence.PowerSequence.GetSequence(baseFunctor, 1, power + 1);
        regression.extend(sequence);
        return regression;