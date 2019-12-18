import unittest

from Approximation.Instruments.Functions import *
from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import PowerFunctor
from Approximation.Instruments.Regressions import PowerRegression

class Test_testPowerRegression(unittest.TestCase):
    def test_GetPowerRegressionReturn1(self):
       baseFunctors = BaseFunctor.BaseFunctor(Return1, [], "");
       power = 10;
       regression = PowerRegression.PowerRegression.GetRegression(baseFunctors, power);
       
       self.assertEqual(power + 1, len(regression));

       constant = BaseFunctor.BaseFunctor(Return1, [], "");
       self.assertEqual(constant, regression[0])

       powerFunctors = PowerFunctor.PowerFunctor(baseFunctors);
       for i in range(1, power + 1):
           powerFunctors.SetPower(i);
           self.assertEqual(powerFunctors, regression[i]);
    
    def test_GetPowerRegressionReturnX(self):
       baseFunctors = BaseFunctor.BaseFunctor(ReturnX, [0], "x");
       power = 10;
       regression = PowerRegression.PowerRegression.GetRegression(baseFunctors, power);
       
       self.assertEqual(power + 1, len(regression));

       constant = BaseFunctor.BaseFunctor(Return1, [], "");
       self.assertEqual(constant, regression[0])

       powerFunctors = PowerFunctor.PowerFunctor(baseFunctors);
       for i in range(1, power + 1):
           powerFunctors.SetPower(i);
           self.assertEqual(powerFunctors, regression[i]);

if __name__ == '__main__':
    unittest.main()
