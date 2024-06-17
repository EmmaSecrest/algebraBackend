#to run tests use python -m unittest discover
import unittest
import sys
sys.path.append('../solve')  

from solve.solve_quadratic import solve_quad_no_factor
from solve.solve_quadratic import set_up_to_solve_quadratic
from solve.solve_quadratic import distribute_negation
from solve.solve_quadratic import splitting_terms
from solve.solve_quadratic import solve_quad_factor
from solve.solve_quadratic import array_factors_coefficient
from solve.solve_quadratic import determine_coefficients
from solve.solve_quadratic import generate_equation_and_solution

class TestDetermineCoefficients(unittest.TestCase):
    def test_determine_coefficients(self):
        self.assertEqual(determine_coefficients(['x**2', '2*x', '3'], 'x'), [1, 2, 3])
        self.assertEqual(determine_coefficients(['2*x**2', '3*x', '4'], 'x'), [2, 3, 4])
        self.assertEqual(determine_coefficients(["x**2","2*x"],'x'), [1,2,0])


class SolveQuadraticNoFactor(unittest.TestCase):
    def test_quadratic_no_factor(self):
        self.assertEqual(solve_quad_no_factor("x**2 + 5*x + 6 = 0"),[  "Use quadratic equation with a = 1, b = 5 and c = 6",['x = -2', 'x = -3']])
        self.assertEqual(solve_quad_no_factor("3*x**2 - 6*x + 7 = 0"), ["Use quadratic equation with a = 3, b = -6 and c = 7", 'No real solutions'])
        self.assertEqual(solve_quad_no_factor("2*x**2 + 4*x + 1 = 0"), ["Use quadratic equation with a = 2, b = 4 and c = 1", ['x = -0.29', 'x = -1.71']])
        self.assertEqual(solve_quad_no_factor("x**2 + x + 1 = 0"), ["Use quadratic equation with a = 1, b = 1 and c = 1", 'No real solutions'])
        self.assertEqual(solve_quad_no_factor("x**2 - 5 = 0"), ["Use quadratic equation with a = 1, b = 0 and c = -5", ['x = 2.24', 'x = -2.24']])

class TestSetUpToSolveQuadratic(unittest.TestCase):
    def test_set_up_to_solve_quadratic(self):
        self.assertEqual(set_up_to_solve_quadratic("x**2 + 3*x+ 2 = 0"), "x**2 + 3*x + 2 = 0")
        self.assertEqual(set_up_to_solve_quadratic("x**2 + 3*x + 2 = -1"), "x**2 + 3*x + 3 = 0")
        self.assertEqual(set_up_to_solve_quadratic("3*x**2 + 4*x + 5 = x**2 - 2*x + 1"), "2*x**2 + 6*x + 4 = 0")

class TestDistributeNegation(unittest.TestCase):
    def test_distribute_negation(self):
        self.assertEqual(distribute_negation("x +2"), "-x-2")
        self.assertEqual(distribute_negation("x -2"), "-x+2")
        self.assertEqual(distribute_negation("-x +2"), "x-2")
        self.assertEqual(distribute_negation("-x -2"), "x+2")

class TestSplittingTerms(unittest.TestCase):
    def test_splitting_terms(self):
        self.assertEqual(splitting_terms("x**2 + x + 1 = 0"), ['x**2', 'x', '1'])
        self.assertEqual(splitting_terms("2*x**2 - 4*x + 1 = 0"), ['2*x**2', '-4*x', '1'])
        self.assertEqual(splitting_terms("x**2 - x - 1 = 0"), ['x**2', '-x', '-1'])
        self.assertEqual(splitting_terms("x**2 + x - 1 = 0"), ['x**2', 'x', '-1'])
        self.assertEqual(splitting_terms("x**2 - x + 1 = 0"), ['x**2', '-x', '1'])
class TestGenerateEquationAndSolution(unittest.TestCase):
    def test_generate_equation_and_solution(self):
        self.assertEqual(generate_equation_and_solution(1,1,2,1,'x'),['(x + 2)(x + 1) = 0', ['x = -2', 'x = -1']])
        self.assertEqual(generate_equation_and_solution(1,1,-2,-1,'x'),['(x - 2)(x - 1) = 0', ['x = 2', 'x = 1']])
        self.assertEqual(generate_equation_and_solution(1,1,-2,1,'x'),['(x - 2)(x + 1) = 0', ['x = 2', 'x = -1']])
        self.assertEqual(generate_equation_and_solution(-1,1,-2,-1,'x'),['(-x - 2)(x - 1) = 0', ['x = -2', 'x = 1']])
        
class TestSolveQuadraticFactor(unittest.TestCase):
    def test_solve_quad_factor(self):
        self.assertEqual(solve_quad_factor("x**2 + 3*x + 2 = 0"), ['(x + 2)(x + 1) = 0', ['x = -2', 'x = -1']])
        self.assertEqual(solve_quad_factor("2*x**2 + 5*x + 3 = 0"), ['(2x + 3)(x + 1) = 0', ['x = -3/2', 'x = -1']])
        self.assertEqual(solve_quad_factor("-3*x**2 + 4*x - 1 = 0"), ['(x - 1)(-3x + 1) = 0', ['x = 1', 'x = 1/3']])
        self.assertEqual(solve_quad_factor("x**2 - 2*x - 8 = 0"), ['(x - 4)(x + 2) = 0', ['x = 4', 'x = -2']])
        self.assertEqual(solve_quad_factor("3*x**2 - 7*x + 2 = 0"), ['(3x - 1)(x - 2) = 0', ['x = 1/3', 'x = 2']])
        self.assertEqual(solve_quad_factor("x**2 -6*x + 9 = 0"), ['(x - 3)(x - 3) = 0', ['x = 3', 'x = 3']])
        self.assertEqual(solve_quad_factor("x**2 - 7*x + 12 = 0"), ['(x - 4)(x - 3) = 0', ['x = 4', 'x = 3']])
        self.assertEqual(solve_quad_factor("x**2 - 8*x + 15 = 0"), ['(x - 5)(x - 3) = 0', ['x = 5', 'x = 3']])
        self.assertEqual(solve_quad_factor("x**2 - 4 = 0"), ['(x + 2)(x - 2) = 0', ['x = -2', 'x = 2']])
        self.assertEqual(solve_quad_factor("x**2 -3*x = 0"), ['x(x - 3) = 0', ['x = 0', 'x = 3']])
        
        
       
class TestArrayFactorsCoefficient(unittest.TestCase):
    def test_array_factors_coefficient(self):
       self.assertEqual(array_factors_coefficient(6), [[1,6],[2,3],[3,2],[6,1]])
       self.assertEqual(array_factors_coefficient(8),  [[1,8],[2,4],[4,2],[8,1]])
       self.assertEqual(array_factors_coefficient(10), [[1,10],[2,5],[5,2],[10,1]])
       self.assertEqual(array_factors_coefficient(12), [[1,12],[2,6],[3,4],[4,3],[6,2],[12,1]])
       self.assertEqual(array_factors_coefficient(-6), [[-3, 2], [-2, 3], [-1, 6], [1, -6], [2, -3], [3, -2]])   

if __name__ == '__main__':
    unittest.main()