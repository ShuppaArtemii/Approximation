import unittest
from Approximation.Instruments import Functions
from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import PowerFunctor
from Approximation import Approximation
import math

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
        functorList.append(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));
        approximation = Approximation.Approximation(parameters, results);
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
        functorList.append(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));

        approximation = Approximation.Approximation(parameters, results);
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
        functorList.append(BaseFunctor.BaseFunctor(Functions.Return1, [], ""));

        approximation = Approximation.Approximation(parameters, results);
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
        functorList.append(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));

        approximation = Approximation.Approximation(parameters, results);
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
        functorList.append(BaseFunctor.BaseFunctor(Functions.Return1, [], ""));
        functorList.append(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));

        approximation = Approximation.Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x_pow_2(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        powerFunctor = PowerFunctor.PowerFunctor(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));
        powerFunctor.SetPower(2);
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation.Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x_pow_3(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [-125, -64, -27, -8, -1, 0, 1, 8, 27, 64, 125];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;

        powerFunctor = PowerFunctor.PowerFunctor(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));
        powerFunctor.SetPower(3);
        functorList = [];
        functorList.append(powerFunctor);
        
        approximation = Approximation.Approximation(parameters, results);
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
        functorList.append(BaseFunctor.BaseFunctor(self.Return1_Div_X, [0], "1/x"));
        
        approximation = Approximation.Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        #self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");
    
    def Return1_Div_X(self, list):
        return 1/list[0];

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
        
        powerFunctor = PowerFunctor.PowerFunctor(BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x"));
        powerFunctor.SetPower(2);
        functorList.append(powerFunctor);
        
        powerFunctor = PowerFunctor.PowerFunctor(BaseFunctor.BaseFunctor(Functions.ReturnX, [1], "y"));
        powerFunctor.SetPower(2);
        functorList.append(powerFunctor);
        
        approximation = Approximation.Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");


    def test_sin_x_pow_2_plus_y_pow_2(self):
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
        results = [-0.262374854,-0.158622669,0.529082686,-0.663633884,0.76255845,-0.13235175,0.76255845,-0.663633884,0.529082686,-0.158622669,-0.262374854,-0.158622669,0.551426681,-0.13235175,0.912945251,-0.961397492,-0.287903317,-0.961397492,0.912945251,-0.13235175,0.551426681,-0.158622669,0.529082686,-0.13235175,-0.750987247,0.420167037,-0.544021111,0.412118485,-0.544021111,0.420167037,-0.750987247,-0.13235175,0.529082686,-0.663633884,0.912945251,0.420167037,0.989358247,-0.958924275,-0.756802495,-0.958924275,0.989358247,0.420167037,0.912945251,-0.663633884,0.76255845,-0.961397492,-0.544021111,-0.958924275,0.909297427,0.841470985,0.909297427,-0.958924275,-0.544021111,-0.961397492,0.76255845,-0.13235175,-0.287903317,0.412118485,-0.756802495,0.841470985,0,0.841470985,-0.756802495,0.412118485,-0.287903317,-0.13235175,0.76255845,-0.961397492,-0.544021111,-0.958924275,0.909297427,0.841470985,0.909297427,-0.958924275,-0.544021111,-0.961397492,0.76255845,-0.663633884,0.912945251,0.420167037,0.989358247,-0.958924275,-0.756802495,-0.958924275,0.989358247,0.420167037,0.912945251,-0.663633884,0.529082686,-0.13235175,-0.750987247,0.420167037,-0.544021111,0.412118485,-0.544021111,0.420167037,-0.750987247,-0.13235175,0.529082686,-0.158622669,0.551426681,-0.13235175,0.912945251,-0.961397492,-0.287903317,-0.961397492,0.912945251,-0.13235175,0.551426681,-0.158622669,-0.262374854,-0.158622669,0.529082686,-0.663633884,0.76255845,-0.13235175,0.76255845,-0.663633884,0.529082686,-0.158622669,-0.262374854];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;
        
        functorList = [];
        functorList.append(BaseFunctor.BaseFunctor(self.ReturnSin_x_pow_2_plus_Y_pow_2, [0, 1], "sin(x^2 + y^2)"));
        
        approximation = Approximation.Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);

        self.assertEqual(len(actualKoefficients), len(expectedKoefficients), "len(actualKoefficients) != len(expectedKoefficients)");
        for i in range(len(actualKoefficients)):
            self.assertAlmostEqual(actualKoefficients[i], expectedKoefficients[i], None, "actualKoefficients[i] !~ expectedKoefficients[i]");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, None, "actualDiscripancy !~ expectedDiscripancy");

    def ReturnSin_x_pow_2_plus_Y_pow_2(self, list):
        return math.sin(math.pow(list[0], 2) + math.pow(list[1], 2));

    def test_hard(self):
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
        results = [-0.262374854,-0.158622669,0.529082686,-0.663633884,0.76255845,-0.13235175,0.76255845,-0.663633884,0.529082686,-0.158622669,-0.262374854,-0.158622669,0.551426681,-0.13235175,0.912945251,-0.961397492,-0.287903317,-0.961397492,0.912945251,-0.13235175,0.551426681,-0.158622669,0.529082686,-0.13235175,-0.750987247,0.420167037,-0.544021111,0.412118485,-0.544021111,0.420167037,-0.750987247,-0.13235175,0.529082686,-0.663633884,0.912945251,0.420167037,0.989358247,-0.958924275,-0.756802495,-0.958924275,0.989358247,0.420167037,0.912945251,-0.663633884,0.76255845,-0.961397492,-0.544021111,-0.958924275,0.909297427,0.841470985,0.909297427,-0.958924275,-0.544021111,-0.961397492,0.76255845,-0.13235175,-0.287903317,0.412118485,-0.756802495,0.841470985,0,0.841470985,-0.756802495,0.412118485,-0.287903317,-0.13235175,0.76255845,-0.961397492,-0.544021111,-0.958924275,0.909297427,0.841470985,0.909297427,-0.958924275,-0.544021111,-0.961397492,0.76255845,-0.663633884,0.912945251,0.420167037,0.989358247,-0.958924275,-0.756802495,-0.958924275,0.989358247,0.420167037,0.912945251,-0.663633884,0.529082686,-0.13235175,-0.750987247,0.420167037,-0.544021111,0.412118485,-0.544021111,0.420167037,-0.750987247,-0.13235175,0.529082686,-0.158622669,0.551426681,-0.13235175,0.912945251,-0.961397492,-0.287903317,-0.961397492,0.912945251,-0.13235175,0.551426681,-0.158622669,-0.262374854,-0.158622669,0.529082686,-0.663633884,0.76255845,-0.13235175,0.76255845,-0.663633884,0.529082686,-0.158622669,-0.262374854];
        expectedKoefficients = [1];
        expectedDiscripancy = 0;
        
        functorList = [];
        functorList.append(BaseFunctor.BaseFunctor(self.ReturnSin_x_pow_2_plus_Y_pow_2, [0, 1], "sin(x^2 + y^2)"));
        
        approximation = Approximation.Approximation(parameters, results);
        actualKoefficients = approximation.CalcKoefficients(functorList);

        self.assertEqual(len(actualKoefficients), len(expectedKoefficients), "len(actualKoefficients) != len(expectedKoefficients)");
        for i in range(len(actualKoefficients)):
            self.assertAlmostEqual(actualKoefficients[i], expectedKoefficients[i], None, "actualKoefficients[i] !~ expectedKoefficients[i]");

        actualDiscripancy = approximation.CalcDiscripancy(actualKoefficients, functorList);
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, None, "actualDiscripancy !~ expectedDiscripancy");


    def Return1_div_1_plus_x_pow_2(self, list):
        return 1 / 1 + math.pow(list[0], 2);

if __name__ == '__main__':
    unittest.main();
