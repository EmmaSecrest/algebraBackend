from unittest import TestCase, main
from fractions import Fraction
from solve.solve_higher_order import (
    solve_synthetic_division,
    array_factors_coefficient_list,
    find_degree,
    is_quadratic_factorable,
    solve_quad_switch,
    determine_coefficients_higher_order,
    put_second_order_back_together,
    determine_possible_zeros,
    synthetic_division,
    convert_to_fraction,
    fraction_to_decimal,
    )



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
        self.assertEqual(determine_coefficients_higher_order("x**5 - x**3 - x + 2 = 0", "x"), {5: 1, 4: 0, 3: -1, 2: 0, 1: -1, 0: 2})    
        self.assertEqual(determine_coefficients_higher_order("x**3 - 4*x -1 = 0", "x"), {3:1,2:0,1:-4,0:-1})

class TestFindDegree(TestCase):
    def test_find_degree(self):
        self.assertEqual(find_degree("x**3 + 2*x**2 - 5*x - 6 = 0", "x"), 3)
        self.assertEqual(find_degree("x**3 - 3*x**2 - 4*x + 12 = 0", "x"), 3)
        self.assertEqual(find_degree("x**5 + x**4 - 15*x**3 - 25*x**2 + 14*x + 24 = 0", "x"), 5)
        self.assertEqual(find_degree("x**2 + 3*x + 2 = 0", "x"), 2)
        self.assertEqual(find_degree("x**2 - 2*x - 8 = 0", "x"), 2)
        self.assertEqual(find_degree("x-4 = 0", "x"), 1 )
        
class TestPutSecondOrderBackTogether(TestCase):
    def test_put_second_order_back_together(self):
        self.assertEqual(put_second_order_back_together({2: 2, 1: -5, 0: -6}, "x"), "2*x**2 - 5*x - 6 = 0")
        self.assertEqual(put_second_order_back_together({2: -3, 1: -4, 0: 12}, "x"), "-3*x**2 - 4*x + 12 = 0")    
        self.assertEqual(put_second_order_back_together({2: 1, 1: 0, 0: 12}, "x"), "x**2 + 12 = 0")        

class TestDeterminePossibleZeros(TestCase):
    def test_determine_possible_zeros(self):
        self.assertEqual(determine_possible_zeros([1,-1],[9,3,1,-1,-3,-9]),[9,3,1,-1,-3,-9])
        self.assertEqual(determine_possible_zeros([2,1,-1,-2],[6,2,1,-1,-2,6]), [3, 1, '1/2', '-1/2', -1, 6, 2, -2, -6, -3])
        self.assertEqual(determine_possible_zeros([2,1,-1,-2],[1,-1]),['1/2', '-1/2', 1, -1])
        
class TestDetermineSyntheticDivision(TestCase):
    def test_synthetic_division(self):
        self.assertEqual(synthetic_division([1, 2,-5,-6], -1), [1, 1, -6,0])
        self.assertEqual(synthetic_division([2,-7,3,8,-4],0.5),[2,-6,0,8,0])
        self.assertEqual(synthetic_division([1,2,2,1],-1),[1,1,1,0])
        self.assertEqual(synthetic_division([1,2.5,3,4,-1.5],-0.5),[1,2,2,3,-3])

class TestConvertToFraction(TestCase):
    def test_convert_to_fraction(self):
        self.assertEqual(convert_to_fraction(0.5), Fraction(1,2))
        self.assertEqual(convert_to_fraction(1.5), Fraction(3,2))
        self.assertEqual(convert_to_fraction(-0.5), Fraction(-1,2))
        self.assertEqual(convert_to_fraction(-1.5), Fraction(-3,2))
        
class TestFractionToDecimal(TestCase):
    def test_fraction_to_decimal(self):
        self.assertEqual(fraction_to_decimal('1/2'), 0.5)
        self.assertEqual(fraction_to_decimal('3/2'), 1.5)
        self.assertEqual(fraction_to_decimal('-1/2'), -0.5)
        self.assertEqual(fraction_to_decimal('-3/2'), -1.5)
        self.assertEqual(fraction_to_decimal('1'),1) 
        self.assertEqual(fraction_to_decimal('1/8'),0.13)
        self.assertEqual(fraction_to_decimal('1/4'),0.25)
        self.assertEqual(fraction_to_decimal('-5'),-5)       

#TODO add a 4th or 5th degree where two zeros are the same
class TestDetermineSyntheticDivision(TestCase):
    def test_synthetic_division(self):
        self.assertEqual(solve_synthetic_division("x**3 + 2*x**2 - 5*x - 6 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-6, -3, -2, -1, 1, 2, 3, 6) then use long division or synthetic division to divide them.",'-3|1 2 -5 -6 ===> 1 -1 -2 | 0', '(-x - 1)(-x + 2) = 0',['x=-3', 'x = -1', 'x = 2']])
        self.assertEqual(solve_synthetic_division("x**3 - 3*x**2 - 4*x + 12 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-12, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 12) then use long division or synthetic division to divide them.",'-2|1 -3 -4 12 ===> 1 -5 6 | 0', '(x - 3)(x - 2) = 0', ['x=-2', 'x = 3', 'x = 2']])
        self.assertEqual(solve_synthetic_division("x**3 - 5*x**2 + 3*x + 9 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-9, -3, -1, 1, 3, 9) then use long division or synthetic division to divide them.",'-1|1 -5 3 9 ===> 1 -6 9 | 0', '(x - 3)(x - 3) = 0', ['x=-1', 'x = 3']])
        self.assertEqual(solve_synthetic_division("x**3 + 3/2*x**2 - 1/2*x -1 = 0"),["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1, 1) then use long division or synthetic division to divide them.",'-1|1 3/2 -1/2 -1 ===> 1 1/2 -1 | 0', 'Use quadratic equation with a = 1, b = 0.5 and c = -1.0', ['x=-1', 'x = 0.78', 'x = -1.28']])
        self.assertEqual(solve_synthetic_division("x**3 - 4*x - 1 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-1, 1) then use long division or synthetic division to divide them.","No rational solution can be found. Brute forcing a solution.", ['x = -0.25', 'x = -1.86', 'x = 2.11']])
        self.assertEqual(solve_synthetic_division("x**3 + 3*x**2 + 4*x + 2 = 0",), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-2, -1, 1, 2) then use long division or synthetic division to divide them.",'-1|1 3 4 2 ===> 1 2 2 | 0', 'Use quadratic equation with a = 1, b = 2 and c = 2', ['x=-1']])
        self.assertEqual(solve_synthetic_division("x**4 + 2*x**3 - 7*x**2 - 8*x + 12 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-12, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 12) then use long division or synthetic division to divide them.",'-3|1 2 -7 -8 12 ===> 1 -1 -4 4 | 0','-2|1 -1 -4 4 ===> 1 -3 2 | 0' ,"(x - 2)(x - 1) = 0", ['x=-3',"x=-2" ,'x = 2', 'x = 1']])
        self.assertEqual(solve_synthetic_division("x**4 + 3*x**3 - 3*x**2 - 7*x + 6 = 0"), ["To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have (-6, -3, -2, -1, 1, 2, 3, 6) then use long division or synthetic division to divide them.",'-3|1 3 -3 -7 6 ===> 1 0 -3 2 | 0', "-2|1 0 -3 2 ===> 1 -2 1 | 0","(x - 1)(x - 1) = 0", ["x=-3","x=-2",'x = 1']])
              
        
if __name__ == '__main__':
    main()