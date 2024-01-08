#to run tests use python -m unittest discover
import unittest
import sys
sys.path.append('../solve')  
from solve.solve_simple_eq import solve_simple_eq

class TestSolveSimpleEq(unittest.TestCase):
    def test_solve_simple_eq(self):
        print(solve_simple_eq("x+1=2"))
        self.assertEqual(solve_simple_eq("x+1=2"),'x=1')
        self.assertEqual(solve_simple_eq("2x-4"),'x=2')
        self.assertEqual(solve_simple_eq("x^2 + 5x + 6"), 'x=-2,x=-3')

if __name__ == '__main__':
    unittest.main()