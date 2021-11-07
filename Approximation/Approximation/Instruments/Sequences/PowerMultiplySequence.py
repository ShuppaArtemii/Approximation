from Approximation.Instruments.Functors.Power import Power
from Approximation.Instruments.FunctorList.Multiplication import Multiplication
from Approximation.Instruments.FunctorList.Sum import Sum

class PowerMultiplySequence:
    def GetSequence(modifiedFunctors : list, start, stop, step = 1):
        sequence = [];
        for power in range(start, stop, step):
            sequence += PowerMultiplySequence.__findNDigitNums(modifiedFunctors, power);

        return Sum(sequence);  

    def __findNDigitNumsUtil(functorListLength, powerSum, out, index, result):
        if (index > functorListLength or powerSum < 0): 
            return

        if (index == functorListLength):
            if(powerSum == 0):
                result.append(out);
            return;
   
        for i in range(powerSum+1): 
            out[index] = i;
            PowerMultiplySequence.__findNDigitNumsUtil(functorListLength, powerSum - i, out.copy(), index + 1, result) 

    def __findNDigitNums(modifiedFunctors, powerSum): 
        functorListLength = len(modifiedFunctors);
        out = [False] * (functorListLength) 
  
        result = [];
        for i in range(0, powerSum+1): 
            out[0] = i;
            PowerMultiplySequence.__findNDigitNumsUtil(functorListLength, powerSum - i, out, 1, result)
        
        sumList = [];
        for i in range(len(result)):
            multiplicationList = [];
            for j in range(len(result[i])):
                if(result[i][j] == 0):
                    continue;
                multiplicationList.append(Power(modifiedFunctors[j], result[i][j]));
            sumList.append(Multiplication(multiplicationList));
        
        result.clear();
        sumList.reverse();
        return sumList;