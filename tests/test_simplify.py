#to run tests use python -m unittest discover


import unittest
import sys
sys.path.append('../simplify')  # Replace '/path/to/simplify' with the actual path to the module
from simplify.simplify_expression import simplify_monomials
from simplify.simplify_expression import simplify_polynomials

class TestSimplifyMonomials(unittest.TestCase):
    def test_simplify_monomials(self):
        # self.assertEqual(expected, simplify_monomials(expression))
        self.assertEqual(simplify_monomials("xxxyz"),'x**3yz')
        self.assertEqual(simplify_monomials("xxxyzxz"),'x**4yz**2')
        self.assertEqual(simplify_monomials("x**2"),'x**2')
        
class TestSimplifyPolynomials(unittest.TestCase):
    def test_simplify_polynomials(self):
        # self.assertEqual(expected, simplify_polynomials(expression))
        self.assertEqual(simplify_polynomials("x**2+x+x+1").replace(" ", ""), "x**2+2*x+1".replace(" ", ""))
        self.assertEqual(simplify_polynomials("x**2+x+x+1+x**2+x+x+1"), "2*x**2 + 4*x + 2")
        self.assertEqual(simplify_polynomials("x-2+1"), "x - 1")
        #test

if __name__ == '__main__':
    unittest.main()