import unittest
from Approximation.Instruments.Functors.X import X;

class testX(unittest.TestCase):
	
	def DefaultX():
		return X(0)

	def BadConstructor(self, params: list):
		try:
			fn = X(params)
			self.fail()
		except ValueError:
			pass

	def test_GetConformity(self):
		fn = testX.DefaultX()
		actual = fn.GetConformity()
		expected = 0
		self.assertEqual(expected, actual)

	def test_BadConstructor1(self):
		self.BadConstructor([])
		
	def test_BadConstructor2(self):
		self.BadConstructor([0, 1])

	def test_Constructor(self):
		fn = DefaultX()

	def test_Call(self):
		 fn = DefaultX()
		 expected = 5
		 actual = fn([expected])
		 self.assertEqual(expected, actual)

	def test_Str(self):
		 fn = DefaultX()
		 actual = str(fn)
		 expected = "x1"
		 self.assertEqual(expected, actual)
	
	def test_ToStringbLatexFalse(self):
		 fn = DefaultX()
		 actual = fn.ToString(bLatex=False)
		 expected = "x1"
		 self.assertEqual(expected, actual)
		 
	def test_ToStringbLatexTrue(self):
		 fn = DefaultX()
		 actual = fn.ToString(bLatex=True)
		 expected = "x_{1}"
		 self.assertEqual(expected, actual)

	def test_EqTrue(self):
		 lhs = DefaultX()
		 rhs = DefaultX()
		 
		 self.assertTrue(lhs == rhs)
	
	def test_EqFalse(self):
		 lhs = X(0)
		 rhs = X([1])
		 
		 self.assertFalse(lhs == rhs)