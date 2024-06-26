from sympy import symbols, degree, Eq, solve, sympify
import math
from fractions import Fraction
from solve.solve_quadratic import (
    determine_coefficients,
    splitting_terms,
    find_symbol,
    solve_quad_no_factor,
    solve_quad_factor,
    format_solution
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
        
def determine_possible_zeros(leading_factors, constant_factors):
    possible_zeros = []
    for leading in leading_factors:
        for constant in constant_factors:
            possible_zero = format_solution(constant/leading)
            if possible_zero.lstrip('-').isdigit():
                possible_zero = int(possible_zero)
            
            if possible_zero not in possible_zeros:
                possible_zeros.append(possible_zero)
            
    return possible_zeros
            
            
            
def synthetic_division(coefficients,zero):
    results = []
    
    i = 0 
    while i<= len(coefficients) - 1:
        if i == 0:
            results.append(coefficients[i])
        else: 
           results.append(zero*results[i-1] + coefficients[i])
        i += 1
    
    return results
    

def convert_to_fraction(x):
    if x % 1 == 0:
        return int(x)
    else:
        return Fraction(x).limit_denominator()  


def solve_synthetic_division(equation):
    solution = []
    
    symbol = find_symbol(equation)
    coefficients = determine_coefficients_higher_order(equation, symbol)
    greatest_degree = max(coefficients.keys())
    leading_coefficient = coefficients[greatest_degree]
    constant = coefficients[0]
    factors_leading_coefficient = array_factors_coefficient_list(leading_coefficient)
    factors_constant = array_factors_coefficient_list(constant)
    possible_zeros = sorted(determine_possible_zeros(factors_leading_coefficient, factors_constant))
    coefficient_values = list(coefficients.values())
    
    
    instructions = "To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have ("
    
    for zero in possible_zeros:
        if zero != possible_zeros[-1]:
            instructions += f"{zero}, "
        else:
            instructions += f"{zero}) then use long division or synthetic division to divide them."
    solution.append(instructions)
    
    results = []
   
        
    while len(coefficient_values) > 3:
        for zero in possible_zeros:
            result = synthetic_division(coefficient_values, zero)
            if result[-1] == 0:
                results.append(f"{symbol}={convert_to_fraction(zero)}")
                solution.append( f"{convert_to_fraction(zero)}|{' '.join(map(str, coefficient_values))} ===> {' '.join(map(str, result[:-1]))} | {result[-1]}")
                coefficient_values = result
                coefficient_values.pop()
                break
            
    new_second_order_eq = put_second_order_back_together({2: coefficient_values[0], 1: coefficient_values[1], 0: coefficient_values[2]}, symbol)
    quad_sol = solve_quad_switch(new_second_order_eq)
    solution.append(quad_sol[0])
    results.append(quad_sol[1][0])
    results.append(quad_sol[1][1])
    solution.append(results)
    
    
        
    
    
    return solution
    