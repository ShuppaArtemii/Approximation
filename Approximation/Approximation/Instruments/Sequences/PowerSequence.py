from  Approximation.Instruments.Functors.Power import Power

class PowerSequence:
    def GetSequence(modifiedFunctors : list, start, stop, step = 1):
        sequence = [];
        for power in range(start, stop, step):
            for i in range(len(modifiedFunctors)):
                powerFunction = Power(modifiedFunctors[i]);
                powerFunction.SetPower(power);
                sequence.append(powerFunction);

        return sequence;  

     
