from Approximation.Instruments.Functors import Power
from Approximation.Instruments.FunctorList import Multiplication, Sum

class PowerMultiplySequence:
    def GetSequence(modifiedFunctors : list, start, stop, step = 1):
        sequence = [];
        for power in range(start, stop, step):
            sequence += PowerMultiplySequence.findNDigitNums_(modifiedFunctors, power);

        return Sum.Sum(sequence);  

    def findNDigitNumsUtil_(functorListLength, powerSum, out, index, result):
        if (index > functorListLength or powerSum < 0): 
            return

        if (index == functorListLength):
            if(powerSum == 0):
                result.append(out);
            return;
   
        for i in range(powerSum+1): 
            out[index] = i;
            PowerMultiplySequence.findNDigitNumsUtil_(functorListLength, powerSum - i, out.copy(), index + 1, result) 

    def findNDigitNums_(modifiedFunctors, powerSum): 
        functorListLength = len(modifiedFunctors);
        out = [False] * (functorListLength) 
  
        result = [];
        for i in range(0, powerSum+1): 
            out[0] = i;
            PowerMultiplySequence.findNDigitNumsUtil_(functorListLength, powerSum - i, out, 1, result)
        
        sumList = [];
        for i in range(len(result)):
            multiplicationList = [];
            for j in range(len(result[i])):
                if(result[i][j] == 0):
                    continue;
                multiplicationList.append(Power.Power(modifiedFunctors[j], result[i][j]));
            sumList.append(Multiplication.Multiplication(multiplicationList));
        
        result.clear();
        sumList.reverse();
        return sumList;