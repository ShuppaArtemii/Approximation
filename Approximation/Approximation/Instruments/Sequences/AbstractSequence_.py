from abc import abstractmethod

class AbstractSequence_:
    @abstractmethod
    def GetSequence(modifiedFunctors : list, start, stop, step = 1):
        sequence = [];
        for index in range(start, stop, step):
            for i in range(len(modifiedFunctors)):
                sequence.append(modifiedFunctors[i]);

        return sequence;