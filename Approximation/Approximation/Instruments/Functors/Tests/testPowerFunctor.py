import unittest
import math
from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import PowerFunctor
from Approximation.Instruments.Functions import *

class Test_PowerFunctor_ReturnX(unittest.TestCase):
    def test_Call(self):
        function = ReturnX;
        conformity = [0];
        strFunction = "x0";

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        powerFunctor = PowerFunctor.PowerFunctor(baseFunctor);
        
        for power in range(0, 3):
            powerFunctor.SetPower(power);
            for i in range(-3, 3):
               self.assertEqual(math.pow(i, power), powerFunctor([i])); 

    def test_ToString(self):
        function = ReturnX;
        conformity = [0];
        strFunction = "x0";

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        powerFunctor = PowerFunctor.PowerFunctor(baseFunctor);
        
        for power in range(0, 3):
            powerFunctor.SetPower(power);
            self.assertEqual(strFunction + "^" + str(power), powerFunctor.ToString());

class Test_PowerFunctor_ReturnX0_Mult_ReturnX1(unittest.TestCase):
    def test_Call(self):
        function = Mult;
        conformity = [0, 1];
        strFunction = "x0*x1";

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        powerFunctor = PowerFunctor.PowerFunctor(baseFunctor);
        
        for power in range(0, 3):
            powerFunctor.SetPower(power);
            for i in range(-3, 3):
                self.assertEqual((math.pow(i, power) * math.pow(i + 5, power)), powerFunctor([i, i + 5]));

    def test_ToString(self):
        function = Mult;
        conformity = [0, 1];
        strFunction = "x0*x1";

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        powerFunctor = PowerFunctor.PowerFunctor(baseFunctor);
        
        for power in range(0, 3):
            powerFunctor.SetPower(power);
            self.assertEqual(strFunction + "^" + str(power), powerFunctor.ToString());


if __name__ == '__main__':
    unittest.main()
