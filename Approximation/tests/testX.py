import unittest
from Approximation.Instruments.Functors.X import X;

class testX(unittest.TestCase):
	
	def DefaultX():
		return X(0)

	def test_GetConformity(self):
		fn = testX.DefaultX()
		actual = fn.GetConformity()
		expected = [0]
		self.assertEqual(expected, actual)

	def test_Constructor(self):
		fn = testX.DefaultX()

	def test_Call(self):
		 fn = testX.DefaultX()
		 expected = 5
		 actual = fn([expected])
		 self.assertEqual(expected, actual)

	def test_Str(self):
		 fn = testX.DefaultX()
		 actual = str(fn)
		 expected = "x1"
		 self.assertEqual(expected, actual)
	
	def test_ToStringbLatexFalse(self):
		 fn = testX.DefaultX()
		 actual = fn.ToString(bLatex=False)
		 expected = "x1"
		 self.assertEqual(expected, actual)
		 
	def test_ToStringbLatexTrue(self):
		 fn = testX.DefaultX()
		 actual = fn.ToString(bLatex=True)
		 expected = "x_{1}"
		 self.assertEqual(expected, actual)

	def test_EqTrue(self):
		 lhs = testX.DefaultX()
		 rhs = testX.DefaultX()
		 
		 self.assertTrue(lhs == rhs)
	
	def test_EqFalse(self):
		 lhs = X(0)
		 rhs = X(1)
		 
		 self.assertFalse(lhs == rhs)

		 
if __name__ == '__main__':
    unittest.main()

