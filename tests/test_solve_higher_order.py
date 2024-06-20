from unittest import TestCase, main

from solve.solve_higher_order import (solve_synthetic_division)

class TestDetermineSyntheticDivision(TestCase):
    def test_synthetic_division(self):
        self.assertEqual(solve_synthetic_division("x**3 + 2*x**2 - 5*x - 6 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1,1,-2,2,-3,3,-6,6) then use long division or synthetic division to divide them.",("x+1","X**2 + x - 6"), ("x-2","x-3"),['x=-1', 'x=2', 'x=3']])
        self.assertEqual(solve_synthetic_division("x**3 - 3*x**2 - 4*x + 12 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1,1,-2,2,-3,3,-4,4,-6,6,-12,12) then use long division or synthetic division to divide them.",("x-3","x**2 - 4"), "(x+2)(x-2)",['x=3', 'x=-2', 'x=2']])
        #(x+1)(x-4)(x+2)(x+3)(x-1)
        self.assertEqual(solve_synthetic_division("x**5 + x**4 - 15*x**3 - 25*x**2 + 14*x + 24 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1,1,-2,2,-3,3,-4,4,-6,6,-8,8,-12,12,-24,24) then use long division or synthetic division to divide them.",
                                                                                                       ("x + 1", "x**4 - 15*x**2 - 10*x + 24"),("x + 2","x**3 - 2*x - 11x + 12"),("x+3", "x**2 - 5*x + 4"),"(x - 4)(x - 1)" ["x=-1", "x=-2", "x=-3", "x=4" ,"x=1" ]])
        