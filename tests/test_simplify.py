from unittest import TestCase, main
from simplify.simplify_expression import simplify_monomials, simplify_polynomials

class TestSimplifyMonomials(TestCase):
    def test_simplify_monomials(self):
        # Create a map of the tested expression and expected result
        test_cases = {
            'xxxyz': 'x**3yz',
            'xxxyzxz': 'x**4yz**2',
            'x**2': 'x**2',
        }
        # Iterate over and run the same function on each case
        for expression, expected in test_cases.items():
            self.assertEqual(simplify_monomials(expression), expected)
        
class TestSimplifyPolynomials(TestCase):
    def test_simplify_polynomials(self):
        # self.assertEqual(expected, simplify_polynomials(expression))
        self.assertEqual(simplify_polynomials("x**2+x+x+1").replace(" ", ""), "x**2+2*x+1".replace(" ", ""))
        self.assertEqual(simplify_polynomials("x**2+x+x+1+x**2+x+x+1"), "2*x**2 + 4*x + 2")
        self.assertEqual(simplify_polynomials("x-2+1"), "x - 1")

if __name__ == '__main__':
    main()
