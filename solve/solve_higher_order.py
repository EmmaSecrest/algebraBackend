from sympy import symbols, degree, Eq, solve, sympify
import math
from solve.solve_quadratic import (
    determine_coefficients,
    splitting_terms,
    find_symbol,
    solve_quad_no_factor,
    solve_quad_factor
    )

def array_factors_coefficient_list(x):
    results = set()
    for i in range(1, abs(x) + 1):
        if x % i == 0:
            results.add(i)
            results.add(-i)
    return sorted(list(results))

def find_degree(equation, symbol):
    s = symbols(symbol)
    left, right = equation.split('=')
    left_side = sympify(left)
    highest_degree = degree(left_side, gen=s)
    
    return highest_degree

def is_quadratic_factorable(equation):
    symbol = find_symbol(equation)
    terms = splitting_terms(equation)
    a, b, c = determine_coefficients(terms, symbol)
    determinate = b**2 - 4*a*c
    
    if determinate < 0:
        return False
    if math.sqrt(determinate) % 1 == 0:
        return True

def solve_quad_switch(equation):
    is_factorable = is_quadratic_factorable(equation)
    if is_factorable:
        return solve_quad_factor(equation)
    else:
        return solve_quad_no_factor(equation)



def solve_synthetic_division(equation):
    pass

