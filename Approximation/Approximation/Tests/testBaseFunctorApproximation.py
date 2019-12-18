import unittest
from Approximation.Instruments import Functions
from Approximation.Instruments.Functors import BaseFunctor

from Approximation import Approximation

class Test_BaseFunctorApproximation(unittest.TestCase):
    def test_Return1(self):
        approximation = Approximation.Approximation();
        approximation.SetParameters([[0]]);
        approximation.SetResults([11]);
        
        baseFunctor = BaseFunctor.BaseFunctor(Functions.Return1, [], "");
        functorsList = [baseFunctor];
        
        koefficients = approximation.CalcKoefficients(functorsList);
        self.assertEqual([11], koefficients);

        discripancy = approximation.CalcDiscripancy(koefficients, functorsList);
        self.assertEqual(0, discripancy);

    def test_Return1_Plus_3ReturnX(self):
        approximation = Approximation.Approximation();
        approximation.SetParameters([[0], [1], [2], [3]]);
        approximation.SetResults([1, 4, 7, 10]);
        
        baseFunctor0 = BaseFunctor.BaseFunctor(Functions.Return1, [], "");
        baseFunctor1 = BaseFunctor.BaseFunctor(Functions.ReturnX, [0], ["x"]);
        functorsList = [baseFunctor0, baseFunctor1];

        koefficients = approximation.CalcKoefficients(functorsList);
        self.assertEqual([1, 3], koefficients);
        
        discripancy = approximation.CalcDiscripancy(koefficients, functorsList);
        self.assertEqual(0, discripancy);

if __name__ == '__main__':
    unittest.main()
