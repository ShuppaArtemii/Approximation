import unittest
from Approximation.Instruments.Functors import BaseFunctor
from Approximation.Instruments.Functors import PowerFunctor
from Approximation.Instruments.Sequences import PowerSequence
from Approximation.Instruments.Functions import *

class Test_testPowerSequence(unittest.TestCase):
    def test_GetSequence(self):
        baseFunctor = BaseFunctor.BaseFunctor(ReturnX, [0], "x0");
       
        start = 0; stop = 5;
        sequence = PowerSequence.PowerSequence.GetSequence([baseFunctor], start, stop);
        self.assertEqual(stop, len(sequence));

        powerFunctor = PowerFunctor.PowerFunctor(baseFunctor);
        for power in range(start, stop):
            powerFunctor.SetPower(power);
            self.assertEqual(powerFunctor, sequence[power]);

if __name__ == '__main__':
    unittest.main()
