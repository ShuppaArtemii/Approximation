import unittest
from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functions import *


class Test_BaseFunctor_Return1(unittest.TestCase):
    def test_Initialization(self):
        function = Return1;
        conformity = [];
        strFunction = "";

        baseFunctors = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        self.assertEqual(function, baseFunctors.function_);
        self.assertEqual(conformity, baseFunctors.conformity_);
        self.assertEqual(strFunction, baseFunctors.strFunction_);

    def test_Call(self):
        function = Return1;
        conformity = [];
        strFunction = "";

        baseFunctors = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        
        for i in range(-3, 3):
            self.assertEqual(1, baseFunctors([i]));

    def test_ToString(self):
        function = Return1;
        conformity = [];
        strFunction = "";

        baseFunctors = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        
        self.assertEqual(strFunction, baseFunctors.ToString());


class Test_BaseFunctor_ReturnX(unittest.TestCase):
    def test_Initialization(self):
        function = ReturnX;
        conformity = [0];
        strFunction = "x0";

        baseFunctors = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        self.assertEqual(function, baseFunctors.function_);
        self.assertEqual(conformity, baseFunctors.conformity_);
        self.assertEqual(strFunction, baseFunctors.strFunction_);

    def test_Call(self):
        function = ReturnX;
        conformity = [0];
        strFunction = "x0";

        baseFunctors = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        
        for i in range(-3, 3):
            self.assertEqual(i, baseFunctors([i]));

    def test_ToString(self):
        function = ReturnX;
        conformity = [0];
        strFunction = "x0";

        baseFunctors = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        
        self.assertEqual(strFunction, baseFunctors.ToString());

class Test_BaseFunctor_Return1_Plus_ReturnX0_Mult_ReturnX1(unittest.TestCase):
    def test_Initialization(self):
        function = Mult;
        conformity = [0, 1];
        strFunction = ["x0*x1"];

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        self.assertEqual(function, baseFunctor.function_);
        self.assertEqual(conformity, baseFunctor.conformity_);
        self.assertEqual(strFunction, baseFunctor.strFunction_);

    def test_Call(self):
        function = Mult;
        conformity = [0, 1];
        strFunction = ["x0*x1"];

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        
        for i in range(-3, 3):
            self.assertEqual(i * (i + 5), baseFunctor([i, i + 5]));

    def test_ToString(self):
        function = Mult;
        conformity = [0, 1];
        strFunction = ["x0*x1"];

        baseFunctor = BaseFunctor.BaseFunctor(function, conformity, strFunction);
        
        self.assertEqual(strFunction, baseFunctor.ToString());


if __name__ == '__main__':
    unittest.main()
