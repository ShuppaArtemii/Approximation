import math
import Chart3D

class Approximation:
    """
    Класс Approximation предназначен для нахождения по некоторым заданным точкам приближенную к ним математическую зависимость
    Прежде чем использовать класс необходимо проинициализировать свойства parameters и results, можно воспользоваться конструктором или соответствующими методами (При необходимости можно вызвать сеттеры снова с другими данными)
    Затем можно безопасно вызывать методы CalcKoefficients - для вычисления коэффициентов зависимости и метод CalcDiscripancy - для вычисления невязки
    Методы оканчивающиеся на подчеркивание '_', не предполагаются к использованию извне класса.
    """
    
#like public methods
    #Constructors
    def __init__(self):
        pass;

    def __init__(self, parameters):
        self.SetParameters(parameters);

    def __init__(self, parameters, results):
        self.SetParameters(parameters);
        self.SetResults(results);
        
    #Setters
    def SetParameters(self, parameters):
        self.parameters = parameters;
    def SetResults(self, results):
        self.results = results;

    #Calc methods
    def CalcKoefficients(self, functions, conformity):
        """
        Метод CalcKoefficients вычисляет коэффициенты зависимости, где тип зависимости(регрессии) определяется в аргументах этого метода
        
        functions - представляет собой тип регрессии. functions имеет тип списка(list), где каждый элемент поддерживает вызов __call__(list) и возвращает некоторое число в качестве результата.
        Метод __call__(list) содержит в своих агументах именно список, чтобы была возможность составления функций с более чем одним агрументом, например это может быть произведение x1 на x2.
        Пример определения functions: [Return1, ReturnX, ReturnX1_Mult_X2], где функции возвращают, что должно быть очевидно, то, что указано у них в названии. Return1, в данном случае,
        используется для представления константы, не зависящей от X. Тогда формула примет вид y = A0*1 + A1*X1 + A2*(X1*X2), а список [A0, A1, A2] будет результатом работы CalcKoefficients.
        
        conformity - определяет какие аргументы будут использоваться при вызове функции из functions. conformity имеет тип списка. Его элементы тоже являются списком и хранят значения
        номеров столбцов parameters, которые должны использоваться при вызове соответсвующей функции.
        Пример определения conformity: [[], [0], [0, 1]], для functions описанных выше.
        
        З.Ы. Возможно, для упрощения составления сложных списков функций стоит использовать функторы, сделав обертку для некоторой функции и при вызове метода __call__ модифицировать
        значения агрументов, например возводя их в нужную степень, а затем вызывая заданую функцию.
        """
        calcMatrix_ = self.InitializeCalcMatrix_(functions, conformity);
        koefficients = self.SolveCalcMatrix_(calcMatrix_);
        return koefficients;
    def CalcDiscripancy(self, koefficients, functions, conformity):
        height_ = len(self.parameters);
        width_ = len(self.parameters[0]);
        squareDiscripancySum = 0;

        for rowIdx in range(0, height_):
            sum = 0;
            for colIdx in range(width_, 0, - 1):
                for funcIdx in range(len(functions)):
                    sum += koefficients[funcIdx] * functions[funcIdx](self.GetFunctionParameters_(rowIdx, conformity[funcIdx]));
            disc = self.results[rowIdx] - sum;
            squareDiscripancySum += disc * disc;

        return squareDiscripancySum;

#like protected methods
    def InitializeCalcMatrix_(self, functions, conformity):
        calcMatrix_ = [];

        for funcIdx1 in range(len(functions)):
            row = [];
            for funcIdx2 in range(len(functions)):
                colomnSum = 0;
                for rowIdx in range(0, len(self.parameters)):
                    colomnSum += functions[funcIdx1](self.GetFunctionParameters_(rowIdx, conformity[funcIdx1])) * functions[funcIdx2](self.GetFunctionParameters_(rowIdx, conformity[funcIdx2]));
                row.append(colomnSum);

            colomnSum = 0;
            for rowIdx in range(0, len(self.parameters)):
                colomnSum += self.results[rowIdx] * functions[funcIdx1](self.GetFunctionParameters_(rowIdx, conformity[funcIdx1]));	
            row.append(colomnSum);
            calcMatrix_.append(row);
            
        return calcMatrix_;
    
    def GetFunctionParameters_(self, rowIdx, conformite):
        row = [];
        for i in range(0, len(conformite)):
           row.append(self.parameters[rowIdx][i]);

        return row;
   
    def SolveCalcMatrix_(self, calcMatrix_):
        height_ = len(calcMatrix_);
        width_ = len(calcMatrix_[0]);

        self.ToUpperTriangularView_(calcMatrix_, height_, width_);
        koefficients_ = [];
        for rowIdx in range(height_ - 1, -1, -1):
            rowSum = 0;
            for k in range(0, width_):
                rowSum += calcMatrix_[rowIdx][k];

            koeff = 2 * calcMatrix_[rowIdx][height_] + 1 - rowSum;
            koefficients_.insert(rowIdx, koeff);
            for colIdx in range(0, rowIdx):
                calcMatrix_[colIdx][rowIdx] *= koeff;

        return koefficients_;

    def ToUpperTriangularView_(self, calcMatrix_, height_, width_):
        for i in range(0, height_):
            for j in range(i, height_):
                if(i == j):
                    value = calcMatrix_[i][j];
                    for k in range(0, width_):
                        calcMatrix_[i][k] /= value;

                elif (i < j):
                    multipleValue = calcMatrix_[j][i];
                    tmpRow = [];
                    for k in range(0, width_):
                        tmpRow.append(calcMatrix_[i][k] * multipleValue);

                    for k in range(0, width_):
                        calcMatrix_[j][k] -= tmpRow[k];

        return;

def Return1(list):
	return 1;

def ReturnX(list):
	return list[0];


if __name__ == '__main__':
    parameters = [
		[2, 0], [3, 0], [4, 0], [5, 0]
	];
    processors = [6, 9, 12, 15];
    ticks = [4, 233, 5016, 128772];

    functions = [Return1, ReturnX];
    conformity = [[], [0]];
    
    approximation = Approximation(parameters, processors);
    koefficients = approximation.CalcKoefficients(functions, conformity);
    discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);

    print("Processors");
    print("Koefficients: ", koefficients);
    print("Discripancy: ", discripancy);
    print();

    Chart3D.Draw(koefficients, functions, -1, 1, 0.1);
    #approximation.SetResults(ticks);
    #koefficients = approximation.CalcKoefficients(functions, conformity);
    #discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);

    #print("Ticks");
    #print("Koefficients: ", koefficients);
    #print("Discripancy: ", discripancy);
    #print();
