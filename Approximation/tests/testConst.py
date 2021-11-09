import unittest
from Approximation.Instruments.Functors.Const import Const;


class testConst(unittest.TestCase):
	def test_Call(self):
		 fn = Const()
		 actual = fn([])
		 expected = 1
		 self.assertEqual(expected, actual)

	def test_Str(self):
		 fn = Const()
		 actual = str(fn)
		 expected = ""
		 self.assertEqual(expected, actual)
	
	def test_ToStringbLatexFalse(self):
		 fn = Const()
		 actual = fn.ToString(bLatex=False)
		 expected = ""
		 self.assertEqual(expected, actual)
		 
	def test_ToStringbLatexTrue(self):
		 fn = Const()
		 actual = fn.ToString(bLatex=True)
		 expected = ""
		 self.assertEqual(expected, actual)

	def test_Eq(self):
		 lhs = Const()
		 rhs = Const()
		 
		 self.assertTrue(lhs == rhs)

		 
if __name__ == '__main__':
    unittest.main()
