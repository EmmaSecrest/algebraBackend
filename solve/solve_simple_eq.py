from sympy import Symbol
from simplify.simplify_expression import simplify_polynomials
import re

def set_up_to_solve(equation):
  # Splitting the equation into two parts
    parts = equation.split('=')
    before_equal = parts[0]
    after_equal = parts[1].strip()

    # Adjust the sign of the constant term
    if after_equal[0] in ['+', '-']:
        new_eq = before_equal + after_equal
    else:
        new_eq = before_equal + '-' + after_equal

    # Simplify the equation
    simplified = simplify_polynomials(new_eq)
    print("simplified: ", simplified)

    return simplified



def solve_simple_eq(equation):
    new_eq = set_up_to_solve(equation)



