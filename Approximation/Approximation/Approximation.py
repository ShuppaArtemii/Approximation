from Approximation.Instruments.FunctorList.AbstractFunctorList import AbstractFunctorList_
from decimal import Decimal
from Approximation.Instruments.FunctorList.Multiplication import Multiplication
import sys

class Approximation:    
    def __init__(self, parameters = None, results = None):
        self.SetParameters(parameters);
        self.SetResults(results);
        
    def SetParameters(self, parameters):
        self.parameters_ = parameters;
    
    def SetResults(self, results):
        self.results_ = results;

    def CalcKoefficients(self, functorList: AbstractFunctorList_):
        calcMatrix_ = self.__InitializeCalcMatrix(functorList);
        koefficients = self.__SolveCalcMatrix(calcMatrix_);
        return koefficients;

    def CalcDiscripancy(self, koefficients, functorList):
        if(len(koefficients) == 0):
            return sys.float_info.max

        height_ = len(self.parameters_);
        width_ = len(self.parameters_[0]);
        squareDiscripancySum = 0;

        for rowIdx in range(0, height_):
            sum = 0;
            for funcIdx in range(len(functorList)):
                sum += Decimal(koefficients[funcIdx]) * functorList[funcIdx](self.parameters_[rowIdx]);
            disc = self.results_[rowIdx] - sum;
            squareDiscripancySum += disc * disc;

        return squareDiscripancySum;

    def __InitializeCalcMatrix(self, functorList):
        calcMatrix_ = [];

        for funcIdx1 in range(len(functorList)):
            func1 = functorList[funcIdx1];
            row = [];
            for funcIdx2 in range(len(functorList)):
                
                func2 = functorList[funcIdx2];
                mult = Multiplication(func1 + func2)
                sum = 0
                for i in range(0, len(self.parameters_)):
                    sum += mult(self.parameters_[i])
               
                row.append(sum);

            colomnSum = 0;
            for rowIdx in range(0, len(self.parameters_)):
                colomnSum += self.results_[rowIdx] * func1(self.parameters_[rowIdx]);
            row.append(colomnSum);
            calcMatrix_.append(row);
            
        return calcMatrix_;
   
    def __SolveCalcMatrix(self, calcMatrix_):
        height_ = len(calcMatrix_);
        width_ = len(calcMatrix_[0]);
        
        koefficients_ = [];
        bResult = self.__ToUpperTriangularView(calcMatrix_, height_, width_);
        if(not bResult):
            return koefficients_;
        
        for rowIdx in range(height_ - 1, -1, -1):
            rowSum = Decimal(0);
            for k in range(0, width_):
                rowSum += calcMatrix_[rowIdx][k];

            koeff = 2 * calcMatrix_[rowIdx][height_] + 1 - rowSum;
            koefficients_.append(koeff);
            for colIdx in range(0, rowIdx):
                calcMatrix_[colIdx][rowIdx] *= koeff;
        koefficients_.reverse();
        return koefficients_;

    def __ToUpperTriangularView(self, calcMatrix_, height_, width_):
        for i in range(0, height_):
            for j in range(i, height_):
                if(i == j):
                    value = calcMatrix_[i][j];
                    if(value == 0):
                        return False;
                    for k in range(0, width_):
                        calcMatrix_[i][k] /= value;

                elif (i < j):
                    multipleValue = calcMatrix_[j][i];
                    tmpRow = [];
                    for k in range(0, width_):
                        tmpRow.append(calcMatrix_[i][k] * multipleValue);

                    for k in range(0, width_):
                        calcMatrix_[j][k] -= tmpRow[k];

        return True;


