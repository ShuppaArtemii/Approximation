from abc import ABC, abstractmethod

class AbstractSequence_:
    @abstractmethod
    def GetSequence(modifiedFunctors, start, stop, step = 1):
        sequence = [];
        for i in range(start, stop, step):
            sequence.append(modifiedFunctors[i]);
        return sequence;