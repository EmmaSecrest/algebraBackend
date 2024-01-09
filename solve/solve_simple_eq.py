from sympy import Symbol
from simplify.simplify_expression import simplify_polynomials
import re

def set_up_to_solve(equation):
    left, right = equation.split('=')
    right = int(right)
    left = simplify_polynomials(left) - right
    return f'{left}=0'



def solve_simple_eq(equation):
    new_eq = set_up_to_solve(equation)


