from Approximation.Instruments.Functors.Const import Const
from Approximation.Instruments.Sequences.PowerMultiplySequence import PowerMultiplySequence
from Approximation.Instruments.FunctorList.Multiplication import Multiplication
from Approximation.Instruments.FunctorList.Sum import Sum
#from Approximation.Instruments.FunctorList.Ceil import Ceil

class PowerMultiplyRegression:
    def GetRegression(functorList : list, power):
        regression = [];
        regression.append(Multiplication([Const()]));
        sequence = PowerMultiplySequence.GetSequence(functorList, 1, power + 1);
        regression.extend(sequence);
        result = Sum(regression);#Ceil(Sum(regression), False);
        return result;
