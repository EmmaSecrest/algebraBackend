from sympy import Symbol, solve
import sys
# sys.path.append('../simplify')
# from simplify.simplify_expression import simplify_polynomials
from simplify.simplify_expression import simplify_polynomials

def solve_simple_eq(equation):
    #simplifying the equation
    #splitting the equation into two parts
     parts = equation.split('=')
     before_equal = parts[0]
     after_equal = parts[1]
     
     print ("before_equal: ", before_equal)
     print ("after_equal: ", after_equal)   
     
test_eq = "x+1=2"
print(solve_simple_eq(test_eq))