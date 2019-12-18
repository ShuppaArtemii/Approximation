from Approximation.Instruments.Sequences import AbstractSequence_
from Approximation.Instruments.Functors import PowerFunctor


class PowerSequence(AbstractSequence_.AbstractSequence_):
    def GetSequence(modifiedFunctors, start, stop, step = 1):
        sequence = [];
        for power in range(start, stop, step):
            powerFunction = PowerFunctor.PowerFunctor(modifiedFunctors);
            powerFunction.SetPower(power);
            sequence.append(powerFunction);
        return sequence;  

     
