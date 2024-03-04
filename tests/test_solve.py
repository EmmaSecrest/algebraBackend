#to run tests use python -m unittest discover
import unittest
import sys
sys.path.append('../solve')  
from solve.solve_linear_eq import solve_linear_y_intercept_eq
from solve.solve_linear_eq import set_up_to_solve
from solve.solve_linear_eq import find_degree
from solve.solve_linear_eq import find_symbol
from solve.solve_quadratic import solve_quad_no_factor
from solve.solve_quadratic import set_up_to_solve_quadratic
from solve.solve_quadratic import distribute_negation
from solve.solve_quadratic import splitting_terms
from solve.solve_quadratic import solve_quad_factor
from solve.solve_quadratic import array_factors_coefficient

class TestSolveLinearYIntercept(unittest.TestCase):
    def solve_linear_y_intercept_eq(self):
        self.assertEqual(solve_linear_y_intercept_eq("x+1=2"),['adding -1 to both sides of the equation', 'x = 1'])
        self.assertEqual(solve_linear_y_intercept_eq("2*x = -4"),[ "dividing each side of the equation by 2",'x = -2.0'])
        self.assertEqual(solve_linear_y_intercept_eq("3*y + 6 = 12"), ['adding -6 to both sides of the equation', "dividing each side of the equation by 3", 'y = 2.0'])
        
class TestFindSymbol(unittest.TestCase):
    def test_find_symbol(self):
        self.assertEqual(find_symbol("x+1=2"), 'x')
        self.assertEqual(find_symbol("2*x = -4"), 'x')
        self.assertEqual(find_symbol("3*y + 6 = 12"), 'y')
        self.assertEqual(find_symbol("a = b"), 'a')
        self.assertEqual(find_symbol("5 + 3 = 8"), None)
        self.assertEqual(find_symbol("2 * 4 = 8"), None)

        
        
class TestSetUpToSolver(unittest.TestCase):
    def test_set_up_to_solve(self):
        self.assertEqual(set_up_to_solve("x+1=2"),'x + 1 = 2')
        self.assertEqual(set_up_to_solve("2*x-4+2=0"),'2*x - 2 = 0')
        self.assertEqual(set_up_to_solve("x**2 + 5*x + 6 + 3*x = 0"), 'x**2 + 8*x + 6 = 0')

class TestHighestDegree(unittest.TestCase):
    def test_highest_degree(self):
        self.assertEqual(find_degree("x + 1 = 2","x"),1)
        self.assertEqual(find_degree("2*x - 4 + 2 = 0","x"),1)
        self.assertEqual(find_degree("x**2 + 5*x + 6 + 3*x = 0","x"), 2)
        self.assertEqual(find_degree("x**3 + x + 1 = 0","x"), 3)

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

class TestSolveQuadraticFactor(unittest.TestCase):
    def test_solve_quad_factor(self):
        self.assertEqual(solve_quad_factor("x**2 + 3*x + 2 = 0"), ['(x + 1)(x + 2) = 0', 'x = -1', 'x = -2'])
        self.assertEqual(solve_quad_factor("2*x**2 + 5*x + 3 = 0"), ['(2x + 1)(x + 3) = 0', 'x = -1', 'x = -3'])
        self.assertEqual(solve_quad_factor("-3*x**2 + 4*x - 1 = 0"), ['(-3x + 1)(x - 1) = 0', 'x = 1', 'x = 1/3'])
        self.assertEqual(solve_quad_factor("x**2 - 2*x - 8 = 0"), ['(x - 4)(x + 2) = 0', 'x = 4', 'x = -2'])
        self.assertEqual(solve_quad_factor("3*x**2 - 7*x + 2 = 0"), ['(3x - 1)(x - 2) = 0', 'x = 1', 'x = 2'])
       
class TestArrayFactorsCoefficient(unittest.TestCase):
    def test_array_factors_coefficient(self):
       self.assertEqual(array_factors_coefficient(6), [[1,6],[2,3],[3,2],[6,1]])
       self.assertEqual(array_factors_coefficient(8),  [[1,8],[2,4],[4,2],[8,1]])
       self.assertEqual(array_factors_coefficient(10), [[1,10],[2,5],[5,2],[10,1]])
       self.assertEqual(array_factors_coefficient(12), [[1,12],[2,6],[3,4],[4,3],[6,2],[12,1]])   
        

if __name__ == '__main__':
    unittest.main()