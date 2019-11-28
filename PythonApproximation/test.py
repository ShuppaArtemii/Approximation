import unittest
import math
import PythonApproximation;

def Return1(list):
	return 1;

def ReturnX(list):
	return list[0];

def Log2(list):
	return math.ceil(math.log2(list[0]));

def Sin(list):
    return math.sin(list[0]);

def Mult(list):
    return list[0]*list[1];

class Test_ExplicitTypeRegression(unittest.TestCase):
    def test_0_plus_3x(self):
        parameters = [ [2], [3], [4], [5] ];
        results = [6, 9, 12, 15];  
        functions = [Return1, ReturnX];
        conformity = [[], [0]];

        approximation = PythonApproximation.Approximation(parameters, results);
        koefficients = approximation.CalcKoefficients(functions, conformity);
        self.assertEqual(koefficients, [0, 3]);
        discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);
        self.assertEqual(discripancy, 0);

    def test_1_plus_log2x(self):
        parameters = [ [2], [3], [4], [5], [6], [7], [8], [9], [15], [20], [25], [30], [35], [40], [45], [50], [100], [150], [200], [250], [300], [350], [400], [450], [500]];
        results = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 10, 10, 10, 10];
        functions = [Return1, Log2];
        conformity = [[], [0]];
        
        approximation = PythonApproximation.Approximation(parameters, results);
        koefficients = approximation.CalcKoefficients(functions, conformity);
        self.assertEqual(koefficients, [1, 1]);
        discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);
        self.assertEqual(discripancy, 0);

    def test_sinx(self):
        pi = math.pi;
        parameters = [ [0], [pi/6], [pi/4], [pi/3], [pi/2], [pi], [3*pi/2], [2*pi]];
        results = [0, 1/2, math.sqrt(2)/2, math.sqrt(3)/2, 1, 0, -1, 0];
        functions = [Sin];
        conformity = [[0]];
        
        approximation = PythonApproximation.Approximation(parameters, results);
        koefficients = approximation.CalcKoefficients(functions, conformity);
        self.assertEqual(koefficients, [1]);
        discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);
        self.assertAlmostEqual(discripancy, 0);

    def test_3_plus_x1_mult_x2(self):
        parameters = [ [0, 0], [0, 1], [1, 0], [1, 1], [3, 2], [4, 5], [10, 1], [7, 11]];
        results = [3, 3, 3, 4, 9, 23, 13, 80];
        functions = [Return1, Mult];
        conformity = [[],[0, 1]];
        
        approximation = PythonApproximation.Approximation(parameters, results);
        koefficients = approximation.CalcKoefficients(functions, conformity);
        self.assertEqual(koefficients, [3, 1]);
        discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);
        self.assertEqual(discripancy, 0);

if __name__ == '__main__':
    unittest.main()
