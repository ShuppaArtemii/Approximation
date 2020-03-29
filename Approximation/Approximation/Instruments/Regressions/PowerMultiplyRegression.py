from Approximation.Instruments.Functors import Const
from Approximation.Instruments.Sequences import PowerMultiplySequence
from Approximation.Instruments.FunctorList import Multiplication, Sum

class PowerMultiplyRegression:
    def GetRegression(functorList : list, power):
        regression = [];
        regression.append(Multiplication.Multiplication([Const.Const()]));
        sequence = PowerMultiplySequence.PowerMultiplySequence.GetSequence(functorList, 1, power + 1);
        regression.extend(sequence);
        sumList = Sum.Sum(regression);
        return sumList;
