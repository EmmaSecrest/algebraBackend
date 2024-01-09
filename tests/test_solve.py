#to run tests use python -m unittest discover
import unittest
import sys
sys.path.append('../solve')  
from solve.solve_simple_eq import solve_simple_eq
from solve.solve_simple_eq import set_up_to_solve

class TestSolveSimpleEq(unittest.TestCase):
    def test_solve_simple_eq(self):
        self.assertEqual(solve_simple_eq("x+1=2"),'x=1')
        self.assertEqual(solve_simple_eq("2*x-4"),'x=2')
        self.assertEqual(solve_simple_eq("x**2 + 5*x + 6"), 'x=-2,x=-3')
        
class TestSetUpToSolver(unittest.TestCase):
    def test_set_up_to_solve(self):
        self.assertEqual(set_up_to_solve("x+1=2"),'x - 1 = 0')
        self.assertEqual(set_up_to_solve("2*x-4+2=0"),'2*x - 2 = 0')
        self.assertEqual(set_up_to_solve("x**2 + 5*x + 6 + 3*x = 0"), 'x**2 + 8*x + 6 = 0')

if __name__ == '__main__':
    unittest.main()