import unittest
from Approximation.Instruments.Functors.X import X
from Approximation.Instruments.Functors.Power import Power
from Approximation.Instruments.Sequences.PowerMultiplySequence import PowerMultiplySequence

class Test_testPowerMultiplySequence(unittest.TestCase):
    def test_GetSequence(self):
        baseFunctor = X(0);
       
        start = 0; stop = 5;
        sequence = PowerMultiplySequence.GetSequence([baseFunctor], start, stop);
        self.assertEqual(stop, len(sequence));

        powerFunctor = Power(baseFunctor, 1);
        for power in range(start, stop):
            powerFunctor.SetPower(power);
            self.assertEqual(powerFunctor, sequence[power]);

if __name__ == '__main__':
    unittest.main()
