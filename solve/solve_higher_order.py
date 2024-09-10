from sympy import symbols, degree, Eq, solve, sympify,re
import math
import re
from collections import Counter
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
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
    

def fraction_to_decimal(fraction_str):
    if fraction_str.lstrip('-').isdigit():
        return int(fraction_str)
    else:
        numerator, denominator = map(int, fraction_str.split('/'))
        decimal = Decimal(numerator) / Decimal(denominator)
        return float(decimal.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))
   
    
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
                coefficients[int(split[1])] = fraction_to_decimal(second_split[0])    
        elif symbol in term and "*" in term and "**" not in term or term == symbol:
            if term == symbol:
                coefficients[1] = 1
            elif split[0] == "-" + symbol:
                coefficients[int(split[1])] = -1    
            else:
                split = term.split("*")
                coefficients[1] = fraction_to_decimal(split[0])
        elif term == symbol:
            coefficients[1] = 1
        elif term == "-" + symbol:
            coefficients[1] = -1  
        elif "**" not in term and "*" not in term and term != symbol:
            coefficients[0] = fraction_to_decimal(term)
    keys = list(coefficients.keys())
    for i in range(0, keys[0]):
        if i not in keys:
            coefficients[i] = 0
          
    return dict(sorted(coefficients.items(),reverse=True))             
            
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
    
    instructions = "To get the possible zeros take the factors of the constant and then divide them by the factors of the leading coefficient in this case we have ("
    instructions += ", ".join(map(str, possible_zeros))
    instructions += ") then use long division or synthetic division to divide them."
    solution.append(instructions)
    
    results = []
    results_unfiltered = []
    coefficient_values = list(coefficients.values())
    
    while len(coefficient_values) > 3:
        found_zero = False
        for zero in possible_zeros:
            result = synthetic_division(coefficient_values, zero)
            if result[-1] == 0:
                found_zero = True
                results.append(f"{symbol}={convert_to_fraction(zero)}")
                solution.append(f"{convert_to_fraction(zero)}|{' '.join(map(str, map(convert_to_fraction, coefficient_values)))} ===> {' '.join(map(str, map(convert_to_fraction, result[:-1])))} | {convert_to_fraction(result[-1])}")
                coefficient_values = result[:-1]  
                break
        if not found_zero:
            solution.append("No rational solution can be found. Brute forcing a solution.")
            left, right = equation.split("=")
            results_unfiltered_non_numerical = solve(left, symbol)
            results_unfiltered = [sol.evalf().as_real_imag()[0] for sol in results_unfiltered_non_numerical]
            break
    
    if results_unfiltered:
        for result in results_unfiltered:
            if result.is_real is not None and result.is_real:
                results.append(f"{symbol} = {round(result, 2)}")
        if not results:
            results.append("No real solutions")
    else:
        new_second_order_eq = put_second_order_back_together({2: coefficient_values[0], 1: coefficient_values[1], 0: coefficient_values[2]}, symbol)
        quad_sol = solve_quad_switch(new_second_order_eq)
        solution.append(quad_sol[0])
        if len(quad_sol[1]) > 1:
            if quad_sol[1][0] == quad_sol[1][1]:
                results.append(quad_sol[1][0])
            if "N" not in quad_sol[1] and "o" not in quad_sol[1]:
                results.extend(quad_sol[1])
        else:
            results.append(quad_sol[1][0])
    
    solution.append(results)
    
    return solution



def solve_sum_diff_of_cubes(equation):
    left, right = equation.split('=')
    symbol = find_symbol(equation)
    coefficients = determine_coefficients_higher_order(equation, symbol)
    solution = []
    results = []
    
    third_order_cube_root = round(abs(coefficients[3]) ** (1/3))
    constant_cube_root = round(abs(coefficients[0]) ** (1/3))
    
    if "+" in left:
        if third_order_cube_root == 1:
            solution.append(f"Use the sum of cubes equation: (a*x + b)(a**2*x**2 - a*b*x + b**2) ===> ({symbol} + {constant_cube_root})({symbol}**2 - {constant_cube_root}*{symbol} + {constant_cube_root**2})")
            results.append(f'{symbol} = {-abs(constant_cube_root)}')
        else:
            solution.append(f"Use the sum of cubes equation: (a*x + b)(a**2*x**2 - a*b*x + b**2) ===> ({third_order_cube_root}*{symbol} + {constant_cube_root})({third_order_cube_root**2}*{symbol}**2 - {constant_cube_root * third_order_cube_root}*{symbol} + {constant_cube_root**2})")
            zero = convert_to_fraction(constant_cube_root/third_order_cube_root)
            results.append(f'{symbol} = {-abs(zero)}')
        
        coefficients = {
            2: third_order_cube_root**2,
            1: -abs(third_order_cube_root * constant_cube_root),
            0: constant_cube_root**2
        }
    elif "-" in left:
        if third_order_cube_root == 1:
            solution.append(f"Use the difference of cubes equation: (a*x - b)(a**2*x**2 + a*b*x + b**2) ===> ({symbol} - {constant_cube_root})({symbol}**2 + {constant_cube_root}*{symbol} + {constant_cube_root**2})")
            results.append(f'{symbol} = {abs(constant_cube_root)}')
        else:
            solution.append(f"Use the difference of cubes equation: (a*x - b)(a**2*x**2 + a*b*x + b**2) ===> ({third_order_cube_root}*{symbol} - {constant_cube_root})({third_order_cube_root**2}*{symbol}**2 + {constant_cube_root * third_order_cube_root}*{symbol} + {constant_cube_root**2})")
            zero = convert_to_fraction(constant_cube_root/third_order_cube_root)
            results.append(f'{symbol} = {abs(zero)}')
        
        coefficients = {
            2: third_order_cube_root**2,
            1: abs(third_order_cube_root * constant_cube_root),
            0: constant_cube_root**2
        }
        
    new_second_order_eq = put_second_order_back_together(coefficients, symbol)
    quad_sol = solve_quad_switch(new_second_order_eq)
    solution.append(quad_sol[0])
   
    results.extend(quad_sol[1])
    
    solution.append(results)
    return solution

def find_common_factor(equation,symbol):
    coefficients = determine_coefficients_higher_order(equation, symbol)
    coefficients_values = list(coefficients.values())
    coefficient_keys = list(coefficients.keys())
    greatest_degree_to_factor_out = 0
    greatest_number_to_factor_out = 1
    degree_string = ""
    print(coefficients_values)
   
    
    for i in range(len(coefficients_values) - 1, -1, -1):
        if coefficients_values[i] == 0:
            greatest_degree_to_factor_out = coefficient_keys[i - 1]
            break
        
    if 0 in coefficients_values:
        coefficients_values.remove(0)
    
    factors_of_coefficients = [factor for value in coefficients_values for factor in array_factors_coefficient_list(value) if factor > 1]
    print("Factors of Coefficients:", factors_of_coefficients)
    factor_counts = Counter(factors_of_coefficients)
    print("Factor Counts:", factor_counts)
    common_factors = [factor for factor, count in factor_counts.items() if count == len(coefficients_values)]
    print("length of coefficient values: ",len(coefficients_values) )
    print("Common Factors:", common_factors)
   
    
    if common_factors:
        greatest_number_to_factor_out = max(common_factors)
    
    if greatest_degree_to_factor_out == 1:
        degree_string = "x"
    elif greatest_degree_to_factor_out > 1:
        degree_string = f"x**{greatest_degree_to_factor_out}"
        
    print(greatest_degree_to_factor_out,greatest_number_to_factor_out)
    
    if greatest_degree_to_factor_out == 0 and greatest_number_to_factor_out ==1:
        return 1
    else:
        if greatest_number_to_factor_out == 1:
            return degree_string
        else:
            return f"{greatest_number_to_factor_out}*{degree_string}"    
   
    
     
        
    

def split_factor_method(equation):
    pass
   
            
            
    
      
        
    
    
