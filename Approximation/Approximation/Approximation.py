
class Approximation:
    """
    Класс Approximation предназначен для нахождения по некоторым заданным точкам приближенную к ним математическую зависимость
    Прежде чем использовать класс необходимо проинициализировать свойства parameters и results, можно воспользоваться конструктором или соответствующими методами (При необходимости можно вызвать сеттеры снова с другими данными)
    Затем можно безопасно вызывать методы CalcKoefficients - для вычисления коэффициентов зависимости и метод CalcDiscripancy - для вычисления невязки
    Методы оканчивающиеся на подчеркивание '_', не предполагаются к использованию извне класса.
    """
    
#like public methods
    #Constructors
    def __init__(self, parameters = None, results = None):
        self.SetParameters(parameters);
        self.SetResults(results);
        
    #Setters
    def SetParameters(self, parameters):
        self.parameters_ = parameters;
    
    def SetResults(self, results):
        self.results_ = results;

    #Calc methods
    def CalcKoefficients(self, functionWithConformity):
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

        calcMatrix_ = self.InitializeCalcMatrix_(functionWithConformity);
        koefficients = self.SolveCalcMatrix_(calcMatrix_);
        return koefficients;

    def CalcDiscripancy(self, koefficients, functionWithConformity):
        """
        Вычисление невязки
        """
        height_ = len(self.parameters_);
        width_ = len(self.parameters_[0]);
        squareDiscripancySum = 0;

        for rowIdx in range(0, height_):
            sum = 0;
            for funcIdx in range(len(functionWithConformity)):
                sum += koefficients[funcIdx] * functionWithConformity[funcIdx](self.GetFunctionParameters_(rowIdx, functionWithConformity[funcIdx].GetConformity()));
            disc = self.results_[rowIdx] - sum;
            squareDiscripancySum += disc * disc;

        return squareDiscripancySum;

#like protected methods
    def InitializeCalcMatrix_(self, functionWithConformity):
        calcMatrix_ = [];

        for funcIdx1 in range(len(functionWithConformity)):
            row = [];
            for funcIdx2 in range(len(functionWithConformity)):
                colomnSum = 0;
                for rowIdx in range(0, len(self.parameters_)):
                    colomnSum += functionWithConformity[funcIdx1](self.GetFunctionParameters_(rowIdx, functionWithConformity[funcIdx1].GetConformity())) * \
                        functionWithConformity[funcIdx2](self.GetFunctionParameters_(rowIdx, functionWithConformity[funcIdx2].GetConformity()));
                row.append(colomnSum);

            colomnSum = 0;
            for rowIdx in range(0, len(self.parameters_)):
                colomnSum += self.results_[rowIdx] * functionWithConformity[funcIdx1](self.GetFunctionParameters_(rowIdx, functionWithConformity[funcIdx1].GetConformity()));	
            row.append(colomnSum);
            calcMatrix_.append(row);
            
        return calcMatrix_;

    def GetFunctionParameters_(self, rowIdx, conformite):     
        row = dict();
        for i in range(0, len(conformite)):
           row[conformite[i]] = self.parameters_[rowIdx][conformite[i]];

        return row;
   
    def SolveCalcMatrix_(self, calcMatrix_):
        height_ = len(calcMatrix_);
        width_ = len(calcMatrix_[0]);
        
        koefficients_ = [];
        bResult = self.ToUpperTriangularView_(calcMatrix_, height_, width_);
        if(not bResult):
            return koefficients_;
        
        for rowIdx in range(height_ - 1, -1, -1):
            rowSum = 0;
            for k in range(0, width_):
                rowSum += calcMatrix_[rowIdx][k];

            koeff = 2 * calcMatrix_[rowIdx][height_] + 1 - rowSum;
            koefficients_.append(koeff);
            for colIdx in range(0, rowIdx):
                calcMatrix_[colIdx][rowIdx] *= koeff;
        koefficients_.reverse();    
        return koefficients_;

    def ToUpperTriangularView_(self, calcMatrix_, height_, width_):
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


