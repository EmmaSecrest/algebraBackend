from unittest import TestCase, main
from solve.solve_higher_order import (
    solve_synthetic_division,
    array_factors_coefficient_list,
    find_degree,
    is_quadratic_factorable,
    solve_quad_switch,
    determine_coefficients_higher_order
    )

# class TestDetermineSyntheticDivision(TestCase):
#     def test_synthetic_division(self):
#         self.assertEqual(solve_synthetic_division("x**3 + 2*x**2 - 5*x - 6 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1,1,-2,2,-3,3,-6,6) then use long division or synthetic division to divide them.","x+1 ===> x**2 + x - 6", "(x-2)(x-3)"],['x=-1', 'x=2', 'x=3']])
#         self.assertEqual(solve_synthetic_division("x**3 - 3*x**2 - 4*x + 12 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1,1,-2,2,-3,3,-4,4,-6,6,-12,12) then use long division or synthetic division to divide them.","x-3 ===> x**2 - 4", "(x+2)(x-2)",['x=3', 'x=-2', 'x=2']])
#         

class TestFactorableQuadratic(TestCase):
    def test_is_quadratic_factorable(self):
        self.assertEqual(is_quadratic_factorable("x**2 + 2*x + 1 = 0"), True)
        self.assertEqual(is_quadratic_factorable("x**2 + 2*x + 2 = 0"), False)

class TestSolveQuadraticSwitch(TestCase):
    def test_solve_quad_switch(self):
        self.assertEqual(solve_quad_switch("x**2 + 3*x + 2 = 0"), ['(x + 2)(x + 1) = 0', ['x = -2', 'x = -1']])
        self.assertEqual(solve_quad_switch("x**2 + 2*x + 2 = 0"),["Use quadratic equation with a = 1, b = 2 and c = 2", 'No real solutions'])

class TestArrayFactorsCoefficientList(TestCase):
    def test_array_factors_coefficient_list(self):
        self.assertEqual(array_factors_coefficient_list(6), [-6, -3, -2, -1, 1, 2, 3, 6])
        self.assertEqual(array_factors_coefficient_list(8), [-8, -4, -2, -1, 1, 2, 4, 8])
        self.assertEqual(array_factors_coefficient_list(10), [-10, -5, -2, -1, 1, 2, 5, 10])
        self.assertEqual(array_factors_coefficient_list(12), [-12, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 12])
        self.assertEqual(array_factors_coefficient_list(-6), [-6, -3, -2, -1, 1, 2, 3, 6])
        self.assertEqual(array_factors_coefficient_list(5), [-5, -1, 1, 5])        
        
class TestDetermineCoefficientsHigherOrder(TestCase):
    def test_determine_coefficients_higher_order(self):
        self.assertEqual(determine_coefficients_higher_order("x**3 + 2*x**2 - 5*x - 6 = 0", "x"), {3: 1, 2: 2, 1: -5, 0: -6})
        self.assertEqual(determine_coefficients_higher_order("x**5 - x**3 - x + 2 = 0", "x"), {5: 1, 3: -1, 1: -1, 0: 2})    

class TestFindDegree(TestCase):
    def test_find_degree(self):
        self.assertEqual(find_degree("x**3 + 2*x**2 - 5*x - 6 = 0", "x"), 3)
        self.assertEqual(find_degree("x**3 - 3*x**2 - 4*x + 12 = 0", "x"), 3)
        self.assertEqual(find_degree("x**5 + x**4 - 15*x**3 - 25*x**2 + 14*x + 24 = 0", "x"), 5)
        self.assertEqual(find_degree("x**2 + 3*x + 2 = 0", "x"), 2)
        self.assertEqual(find_degree("x**2 - 2*x - 8 = 0", "x"), 2)
        self.assertEqual(find_degree("x-4 = 0", "x"), 1 )
        
if __name__ == '__main__':
    main()