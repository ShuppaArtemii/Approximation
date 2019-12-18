from FunctorsBuilder import AbstractSequence_ 
from FunctorsBuilder import PowerFunction

class PowerSequence(AbstractSequence_.AbstractSequence_):
    def GetSequence(modifiedFunctors, start, stop, step = 1):
        sequence = [];
        for power in range(start, stop, step):
            for funcIdx in range(len(modifiedFunctors)):
                powerFunction = PowerFunction.PowerFunction(modifiedFunctors[funcIdx].function, baseFunction[funcIdx].conformity);
                powerFunction.SetPower(power);
                sequence.append(powerFunction);
        return sequence;  

     