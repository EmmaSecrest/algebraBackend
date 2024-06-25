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

def determine_coefficients_higher_order(equation,symbol):
    terms = splitting_terms(equation)
    coefficients = {}
    
    for term in terms:
        if "**" in term:
            split = term.split("**")
            if split[0] == symbol:
                coefficients[int(split[1])] = 1
            elif split[0] == "-" + symbol:
                coefficients[int(split[1])] = -1    
            else:
                second_split = split[0].split("*")
                coefficients[int(split[1])] = int(second_split[0])    
        elif symbol in term and "*" in term and "**" not in term or term == symbol:
            if term == symbol:
                coefficients[1] = 1
            elif split[0] == "-" + symbol:
                coefficients[int(split[1])] = -1    
            else:
                split = term.split("*")
                coefficients[1] = int(split[0])
        elif term == symbol:
            coefficients[1] = 1
        elif term == "-" + symbol:
            coefficients[1] = -1  
        elif "**" not in term and "*" not in term and term != symbol:
            coefficients[0] = int(term)         
            
    return coefficients                
            
def put_second_order_back_together(coefficients, symbol):
    equation = ""
    for key, value in sorted(coefficients.items(), reverse=True):
        if key == 0:
            if value < 0:
                equation += f"- {abs(value)} = 0"
            else:
                equation += f"+ {value} = 0"
                
        elif key == 2:
            if value == 1:
                equation += f"{symbol}**2 " 
            elif value == -1:
                equation += f"- {symbol}**2 "
            else:
                equation += f"{value}*{symbol}**2 "
        
        else:  # key == 1
            if value == 0:
                continue
            elif value == 1:
                equation += f"+ {symbol} "
            elif value == -1:
                equation += f"- {symbol} "
            elif value < 0:
                equation += f"- {abs(value)}*{symbol} "
            else:
                equation += f"+ {value}*{symbol} "
           
    return equation     
        
    

def solve_synthetic_division(equation):
    pass

