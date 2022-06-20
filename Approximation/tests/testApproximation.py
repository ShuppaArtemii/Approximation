import unittest
from Approximation.AutoApproximation import AutoApproximation
from Approximation.OutputData import OutputData

class Test_Approximation(unittest.TestCase):
    def Check(self, parameters, processors, expectedString, expectedDiscripancy):
        koeff, func, disc = AutoApproximation.Analyse(parameters.copy(), processors.copy())
        ouputData = OutputData(koeff, func, [], [])
        actualString = ouputData.data["data_width"]
        
        self.assertAlmostEqual(disc, expectedDiscripancy, 7, "actualDiscripancy != expectedDiscripancy");
        self.assertEqual(actualString, expectedString, "actualString != expectedString");
    
    def test_100(self):
        parameters = [[0]]
        processors = [100]
        
        expectedString = "100.0";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)
        
    def test_1_plus_3x(self):
        parameters = [[1], [2], [3]]
        processors = [4, 7, 10]
        
        expectedString = "1.0 + 3.0*x1";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)

    def test_2_plus_log2x(self):
        parameters = [[1], [2], [3], [4], [5]]
        processors = [2, 3, 99, 224, 425]
        
        expectedString = "2.0 + 1.0*log2(x1)";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)


    def test_ex(self):
        parameters = [[1], [2], [3], [4], [5], [6]]
        processors = [3, 8, 21, 55, 149, 404]
        
        expectedString = "1.0*exp(x1)";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)

    def test_pow_x_10(self):
        parameters = [[1], [2], [3], [4], [5], [6]]
        processors = [1, 1024, 59049, 1048576, 9765625, 60466176]
        
        expectedString = "1.0*x1^10";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)


    def test_x1_mult_x2(self):
        parameters = [[1, 1], [1, 2], [2, 1], [2, 3], [3, 2], [3, 3]]
        processors = [1, 2, 2, 6, 6, 9]
        
        expectedString = "1.0*x1*x2";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)

    def test_x1_2_plus_x1x2_plus_x2_2(self):
        parameters = [[1, 1], [1, 2], [2, 1], [2, 3], [3, 2], [3, 3]]
        processors = [3, 7, 7, 19, 19, 27]
        
        expectedString = "1.0*x1^2 + 1.0*x1*x2 + 1.0*x2^2";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)

    def test_x1_2_plus_x2_3_plus_x1_4_plus_x2_5(self):
        parameters = [[1, 1], [1, 2], [2, 1], [2, 3], [3, 2], [3, 3]]
        processors = [4, 42, 22, 290, 130, 360]
        
        expectedString = "1.0*x1^2 + 1.0*x2^3 + 1.0*x1^4 + 1.0*x2^5";
        expectedDiscripancy = 0;

        self.Check(parameters, processors, expectedString, expectedDiscripancy)

if __name__ == '__main__':
    unittest.main();
