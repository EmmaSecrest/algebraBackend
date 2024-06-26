#to run tests use python -m unittest discover
from unittest import TestCase, main

from solve.solve_linear_eq import (
    solve_linear_y_intercept_eq,
    set_up_to_solve,

    find_symbol,
)


class TestSolveLinearYIntercept(TestCase):
    def solve_linear_y_intercept_eq(self):
        self.assertEqual(solve_linear_y_intercept_eq("x+1=2"),['adding -1 to both sides of the equation', 'x = 1'])
        self.assertEqual(solve_linear_y_intercept_eq("2*x = -4"),[ "dividing each side of the equation by 2",'x = -2.0'])
        self.assertEqual(solve_linear_y_intercept_eq("3*y + 6 = 12"), ['adding -6 to both sides of the equation', "dividing each side of the equation by 3", 'y = 2.0'])
        self.assertEqual(solve_linear_y_intercept_eq("x - 3 = 0"), ['adding 3 to both sides of the equation', 'x = 3'])


class TestFindSymbol(TestCase):
    def test_find_symbol(self):
        self.assertEqual(find_symbol("x+1=2"), 'x')
        self.assertEqual(find_symbol("2*x = -4"), 'x')
        self.assertEqual(find_symbol("3*y + 6 = 12"), 'y')
        self.assertEqual(find_symbol("a = b"), 'a')
        self.assertEqual(find_symbol("5 + 3 = 8"), None)
        self.assertEqual(find_symbol("2 * 4 = 8"), None)
class TestSetUpToSolver(TestCase):
    def test_set_up_to_solve(self):
        self.assertEqual(set_up_to_solve("x+1=2"),'x + 1 = 2')
        self.assertEqual(set_up_to_solve("2*x-4+2=0"),'2*x - 2 = 0')
        self.assertEqual(set_up_to_solve("x**2 + 5*x + 6 + 3*x = 0"), 'x**2 + 8*x + 6 = 0')

if __name__ == '__main__':
    main()
