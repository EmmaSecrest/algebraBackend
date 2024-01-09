from sympy import Symbol
from simplify.simplify_expression import simplify_polynomials
import re

def set_up_to_solve(equation):
    left, right = equation.split('=')
    # Simplify the left and right sides of the equation
    left = simplify_polynomials(left)
    right = simplify_polynomials(right)
    # Subtract the right side from the left side and simplify the result
    simplified = simplify_polynomials(f'{left} - ({right})')
    return f'{simplified} = 0'



def solve_simple_eq(equation):
    new_eq = set_up_to_solve(equation)


