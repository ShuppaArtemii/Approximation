import unittest
from Approximation.Instruments.Functors.X import X;
from Approximation.Instruments.Functors.Power import Power;

class testPower(unittest.TestCase):
	def BadConstructor(self, internalFunctor, power):
		try:
			fn = Power(internalFunctor, power)
			self.fail()
		except ValueError:
			pass

	def test_Constructor(self):
		fn = Power(X(0), 2)

	def test_Call1(self):
		 fn = Power(X(0), 2)
		 expected = 25
		 actual = fn([5])
		 self.assertEqual(expected, actual)
		 
	def test_Call2(self):
		 fn = Power(X(0), 1/2)
		 expected = 7
		 actual = fn([49])
		 self.assertEqual(expected, actual)

	def test_Str(self):
		 fn = Power(X(0), 2)
		 actual = str(fn)
		 expected = "x1^2"
		 self.assertEqual(expected, actual)
	
	def test_ToStringbLatexFalse(self):
		 fn = Power(X(0), 2)
		 actual = fn.ToString(bLatex=False)
		 expected = "x1^2"
		 self.assertEqual(expected, actual)
		 
	def test_ToStringbLatexTrue(self):
		 fn = Power(X(0), 2)
		 actual = fn.ToString(bLatex=True)
		 expected = "x_{1}^{2}"
		 self.assertEqual(expected, actual)

	def test_EqTrue(self):
		 lhs = Power(X(0), 2)
		 rhs = Power(X(0), 2)
		 
		 self.assertTrue(lhs == rhs)
	
	def test_EqFalse1(self):
		 lhs = Power(X(0), 2)
		 rhs = Power(X(0), 3)
		 
		 self.assertFalse(lhs == rhs)
	
	def test_EqFalse2(self):
		 lhs = Power(X(0), 2)
		 rhs = Power(X(1), 2)
		 
		 self.assertFalse(lhs == rhs)
		 
if __name__ == '__main__':
    unittest.main()