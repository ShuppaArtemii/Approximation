import unittest
from Approximation.Instruments.Functors.Const import Const
from Approximation.Instruments.Functors.X import X
from Approximation.Instruments.Functors.Power import Power
from Approximation.Instruments.Functors.Log2 import Log2
from Approximation.Instruments.Functors.Ceil import Ceil
from Approximation.Instruments.Functors.Exp import Exp
from Approximation.Approximation import Approximation
from Approximation.Instruments.Regressions.PowerMultiplyRegression import PowerMultiplyRegression

#Тестирование класса Approximation. В каждом методе (CalcKoefficients) запрашиваем у класса вычисление
#коэффициентов для данных, с заранее определенным типом зависимости. При этом в этом методе
#передаем соответствующий входным данным тип зависимости, явно его указывая, тем самым, всегда получая
#строго определенные результаты. Тестирование в данном случае должно продемонстрировать возможность
#работы с различными видами зависимостей, с различными наборами входных параметров, возможными
#ошибками, которые могут возникнуть входе работы

class Test_testApproximation(unittest.TestCase):
    
    def test_special_ResultsInputError(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [-5, -4, -3,-2,-1, 0, 1, 2, 3, 4];#без одного значения
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        functorList = [];
        functorList.append(X(0));
        approximation = Approximation(parameters, results);
        try:
            actualKoefficients = approximation.CalcKoefficients(functorList);#выбрасывает исключение
        except IndexError:
            return;
        self.fail("Не было выброшено исключение");
        
   
    def test_special_ParametersInputError(self):
        parameters = [[-5],[-4],[-3],[-2],[-1], [1],[2],[3],[4],[5]];#без одного значения
        results = [-5, -4, -3,-2,-1, 0, 1, 2, 3, 4, 5];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        functorList = [];
        functorList.append(X(0));

        approximation = Approximation(parameters, results);
        try:
            actualKoefficients = approximation.CalcKoefficients(functorList);#выбрасывает исключение
        except IndexError:
            return;
        self.fail("Не было выброшено исключение");

    def test_11(self):
        parameters = [[0]];
        results = [11];
        expectedKoefficients = [11];
        expectedDiscripancy = 0;

        functorList = [];
        functorList.append(Const());

        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [-5, -4, -3,-2,-1, 0, 1, 2, 3, 4, 5];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        functorList = [];
        functorList.append(X(0));

        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_7_plus_3x(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [-8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22];
        expectedKoefficients = [7, 3];
        expectedDiscripancy = 0;

        functorList = [];
        functorList.append(Const());
        functorList.append(X(0));

        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x_pow_2(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        powerFunctor = Power(X(0), 2);
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x_pow_3(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [-125, -64, -27, -8, -1, 0, 1, 8, 27, 64, 125];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        powerFunctor = Power(X(0), 3);
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_1_div_x(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[1],[2],[3],[4],[5]];
        results = [-0.2, -0.25, -1/3, -0.5, -1, 1, 0.5, 1/3, 0.25, 0.2];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        functorList = [];
        functorList.append(Power(X(0), -1));
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        #self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x_pow2_plus_y_pow_2(self):
        parameters = [[-5,-5],[-5,-4],[-5,-3],[-5,-2],[-5,-1],[-5,-0],[-5,1],[-5,2],[-5,3],[-5,4],[-5,5],
                       [-4,-5],[-4,-4],[-4,-3],[-4,-2],[-4,-1],[-4,-0],[-4,1],[-4,2],[-4,3],[-4,4],[-4,5],
                       [-3,-5],[-3,-4],[-3,-3],[-3,-2],[-3,-1],[-3,-0],[-3,1],[-3,2],[-3,3],[-3,4],[-3,5],
                       [-2,-5],[-2,-4],[-2,-3],[-2,-2],[-2,-1],[-2,-0],[-2,1],[-2,2],[-2,3],[-2,4],[-2,5],
                       [-1,-5],[-1,-4],[-1,-3],[-1,-2],[-1,-1],[-1,-0],[-1,1],[-1,2],[-1,3],[-1,4],[-1,5],
                       [0,-5],[0,-4],[0,-3],[0,-2],[0,-1],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],
                       [1,-5],[1,-4],[1,-3],[1,-2],[1,-1],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],
                       [2,-5],[2,-4],[2,-3],[2,-2],[2,-1],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],
                       [3,-5],[3,-4],[3,-3],[3,-2],[3,-1],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],
                       [4,-5],[4,-4],[4,-3],[4,-2],[4,-1],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],
                       [5,-5],[5,-4],[5,-3],[5,-2],[5,-1],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]];
        results = [50,41,34,29,26,25,26,29,34,41,50,41,32,25,20,17,16,17,20,25,32,41,34,25,18,13,10,9,10,13,18,25,34,29,20,13,8,5,4,5,8,13,20,29,26,17,10,5,2,1,2,5,10,17,26,25,16,9,4,1,0,1,4,9,16,25,26,17,10,5,2,1,2,5,10,17,26,29,20,13,8,5,4,5,8,13,20,29,34,25,18,13,10,9,10,13,18,25,34,41,32,25,20,17,16,17,20,25,32,41,50,41,34,29,26,25,26,29,34,41,50];
        expectedKoefficients = [1, 1];
        expectedDiscripancy = 0;
        
        functorList = [];
        
        
        powerFunctor = Power(X(0), 2);
        functorList.append(powerFunctor);
        
        
        powerFunctor = Power(X([1]), 2);
        functorList.append(powerFunctor);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");


    def test_log2x(self):
        parameters = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]];
        results = [0, 1, 1.58496250072116, 2, 2.32192809488736, 2.58496250072116, 2.8073549220576, 3,3.16992500144231, 3.32192809488736, 3.4594316186373];
        expectedKoefficients = [1];
        expectedDiscripancy = 0.;

        powerFunctor = Log2(X(0));
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

    def test_ceilLog2x(self):
        parameters = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]];
        results = [0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4];
        expectedKoefficients = [1];
        expectedDiscripancy = 0.;

        powerFunctor = Ceil(Log2(X(0)));
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

    def test_expX(self):
        parameters = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]];
        results = [1,
            2.71828182845904,
            7.38905609893065,
            20.0855369231877,
            54.5981500331442,
            148.413159102577,
            403.428793492735,
            1096.63315842846,
            2980.95798704173,
            8103.08392757538,
            22026.4657948067,
            59874.1417151978
        ];
        expectedKoefficients = [1];
        expectedDiscripancy = 0.;

        
        functorList = PowerMultiplyRegression.GetRegression([Exp(X(0))], 1);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

    def test_ceilExpX(self):
        parameters = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]];
        results = [3, 8, 21, 55, 149, 404, 1097, 2981, 8104, 22027, 59875];
        expectedKoefficients = [1];
        expectedDiscripancy = 0.;

        powerFunctor = Ceil(Exp(X(0)));
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

    def test_20(self):
        #From
        #Algorithm for solving a quadratic equation
        parameters = [[0, 0]]
        processors = [20]
        
        expectedKoefficients = [20];
        expectedDiscripancy = 0.;

        functorList = [];
        functorList.append(Const());

        approximation = Approximation(parameters, processors);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

if __name__ == '__main__':
    unittest.main();
