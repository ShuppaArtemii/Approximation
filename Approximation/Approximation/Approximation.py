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

    def CalcKoefficients(self, functionWithConformity: AbstractFunctorList_):
        calcMatrix_ = self.__InitializeCalcMatrix(functionWithConformity);
        koefficients = self.__SolveCalcMatrix(calcMatrix_);
        return koefficients;

    def CalcDiscripancy(self, koefficients, functionWithConformity):
        if(len(koefficients) == 0):
            return sys.float_info.max

        height_ = len(self.parameters_);
        width_ = len(self.parameters_[0]);
        squareDiscripancySum = 0;

        for rowIdx in range(0, height_):
            #sum = functionWithConformity(self.parameters_[rowIdx])
            sum = 0;
            for funcIdx in range(len(functionWithConformity)):
                sum += koefficients[funcIdx] * Decimal(functionWithConformity[funcIdx](self.parameters_[rowIdx]));
            disc = self.results_[rowIdx] - sum;
            squareDiscripancySum += disc * disc;

        return squareDiscripancySum;

    def __InitializeCalcMatrix(self, functionWithConformity):
        calcMatrix_ = [];

        for funcIdx1 in range(len(functionWithConformity)):
            func1 = functionWithConformity[funcIdx1];
            row = [];
            for funcIdx2 in range(len(functionWithConformity)):
                
                func2 = functionWithConformity[funcIdx2];
                mult = Multiplication(func1 + func2)
                sum = 0
                for i in range(0, len(self.parameters_)):
                    sum += mult(self.parameters_[i])
                
                
                #colomnSum = 0;
                #for rowIdx in range(0, len(self.parameters_)):
                #    colomnSum += Decimal(functionWithConformity[funcIdx1](self.__GetFunctionParameters(func1, self.parameters_))) * \
                #        Decimal(functionWithConformity[funcIdx2](self.parameters_[func2.GetConformity()]));
                row.append(sum);

            colomnSum = 0;
            for rowIdx in range(0, len(self.parameters_)):
                colomnSum += self.results_[rowIdx] * func1(self.parameters_[rowIdx]);
            row.append(colomnSum);
            calcMatrix_.append(row);
            
        return calcMatrix_;

    def __GetFunctionParameters(self, rowIdx, conformite):     
        row = [];
        for i in range(0, len(conformite)):
           row[conformite[i]] = self.parameters_[rowIdx][conformite[i]];

        return row;

    def __GetFunctionParameters(self, func, parameters):
        conf = func.GetConformity();
        row = dict();
        for i in range(0, len(conformite)):
           row[conformite[i]] = self.parameters_[rowIdx][conformite[i]];

        return row;
   
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


