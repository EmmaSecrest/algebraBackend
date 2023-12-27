import unittest
import sys
sys.path.append('../simplify')  # Replace '/path/to/simplify' with the actual path to the module
from simplify.simplify_monomials import simplify_monomials

class TestSimplifyMonomials(unittest.TestCase):
    def test_simplify_monomials(self):
        # self.assertEqual(expected, simplify_monomials(expression))
        self.assertEqual(simplify_monomials("xxxyz"),'x^3yz')
        self.assertEqual(simplify_monomials("xxxyzxz"),'x^4yz^2')
if __name__ == '__main__':
    unittest.main()