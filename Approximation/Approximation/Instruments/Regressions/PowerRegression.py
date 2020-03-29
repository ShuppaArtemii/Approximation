from Approximation.Instruments.Functors.Const import Const
from Approximation.Instruments.Sequences.PowerSequence import PowerSequence


class PowerRegression:
    def GetRegression(baseFunctor : list, power):
        regression = [];
        regression.append(Const());
        sequence = PowerSequence.GetSequence(baseFunctor, 1, power + 1);
        regression.extend(sequence);
        return regression;