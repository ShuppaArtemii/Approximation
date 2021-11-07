from Approximation.Instruments.Functors.Const import Const
from Approximation.Instruments.Sequences.PowerMultiplySequence import PowerMultiplySequence
from Approximation.Instruments.FunctorList.Multiplication import Multiplication
from Approximation.Instruments.FunctorList.Sum import Sum

class PowerMultiplyRegression:
    def GetRegression(functorList : list, power):
        regression = [];
        regression.append(Multiplication([Const()]));
        sequence = PowerMultiplySequence.GetSequence(functorList, 1, power + 1);
        regression.extend(sequence);
        result = Sum(regression);
        return result;
