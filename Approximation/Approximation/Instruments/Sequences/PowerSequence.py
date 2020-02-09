from Approximation.Instruments.Sequences import AbstractSequence_
from Approximation.Instruments.Functors import PowerFunctor


class PowerSequence(AbstractSequence_.AbstractSequence_):
    def GetSequence(modifiedFunctors : list, start, stop, step = 1):
        sequence = [];
        for power in range(start, stop, step):
            for i in range(len(modifiedFunctors)):
                powerFunction = PowerFunctor.PowerFunctor(modifiedFunctors[i]);
                powerFunction.SetPower(power);
                sequence.append(powerFunction);

        return sequence;  

     
