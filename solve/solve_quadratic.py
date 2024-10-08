from simplify.simplify_expression import simplify_polynomials
from sympy import symbols, degree, Eq, solve,sqrt,simplify
import re
import math
from solve.solve_linear_eq import solve_linear_y_intercept_eq
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP

def distribute_negation(expression):
    split = re.split(" ",expression)
    if len(split) >1:
        for index, term in enumerate(split):
            if index != 0 and term.startswith('-'):
                split[index] = term.replace('-', '+')
            elif index != 0 and term.startswith('+'):
                split[index] = term.replace('+', '-')
            elif index == 0 and not term.startswith('-'):
                split[index] = '-' + term
            elif index == 0 and term.startswith('-'):
                split[index] = term.replace('-', '')
    else:
        if split[0].startswith('-'):
            split[0] = split[0].replace('-', '+')
        else:
            split[0] = '-' + split[0]
    
    
    result = ''.join(split)
    return result

def find_symbol(equation):
    # This regular expression matches any non-numeric and non-operator character
    matches = re.findall(r'[^\d\+\-\*\/\=\s]', equation)
    # Filter out any empty strings
    symbols = [match for match in matches if match]
    return symbols[0] if symbols else None

# def set_up_to_solve_quadratic(equation):
#     left, right = equation.split('=')
#     left = simplify_polynomials(left)
#     right = simplify_polynomials(right)
#     # Distribute the negation across the right side
#     right = distribute_negation(right)
#     result = left + right
#     result = simplify_polynomials(result)
#     result = result + " = 0"
#     return result

def splitting_terms(equation):
    left, right = equation.split('=')
    split = left.split(" ")
    terms = []
    
    if split[len(split)-1] == "" or split[len(split)-1] == " ":
        split.pop()
    
    for i in range(len(split)):
        if split[i] not in terms:
            if split[i] == "-":
                split[i+1] = "-" + split[i+1]
                terms.append(split[i+1])
                continue
            if split[i] != "+" and split[i] != "-":
                terms.append(split[i])
        else:
            continue
         
    return terms

def quadratic_formula(a, b, c):
    determinate = b**2 - 4*a*c
    if determinate < 0:
        return "No real solutions"
    else:
        part_1 = sqrt(determinate)
        part_2 = 2*a
        solution_1 = (-b + part_1) / part_2
        solution_2 = (-b - part_1) / part_2
        solutions = [simplify(solution_1), simplify(solution_2)]
        
        if solution_1 == solution_2:
            return solution_1
        else:
            return solutions
                
       
def determine_coefficients(terms, symbol):
    a = 1
    b  = 0
    c = 0
    
    for term in terms:
        
        #finding the coefficient of a
        if "**2" in term:
            split = term.split("**")
            
            if len(split[0]) > 1:
                second_split = split[0].split("*")
                if second_split[0].lstrip('-').isdigit():
                   a = int(second_split[0])
                else:
                    try:
                    # Try to convert to float
                        a = float(second_split[0])
                    except ValueError:
                        # If it fails, handle as fraction
                        numerator, denominator = map(int,second_split[0].split('/'))
                        decimal = Decimal(numerator) / Decimal(denominator)
                        a = float(decimal.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))     
                
            elif split[0] == symbol:
                a = 1    
            else:
                print("split 0", split[0])
        #finding the coefficient of b
        elif symbol in term and "*" in term and "**2" not in term or term == symbol or term == "-" + symbol:
            if term == symbol:
                b = 1
            elif term == "-" + symbol:
                b = -1    
            else:
                split = term.split("*")
                if split[0].lstrip('-').isdigit():
                    b = int(split[0])
                else:
                    try:
                        # Try to convert to float
                        b = float(split[0])
                    except ValueError:
                        # If it fails, handle as fraction
                        numerator, denominator = map(int,split[0].split('/'))
                        decimal = Decimal(numerator) / Decimal(denominator)
                        b = float(decimal.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))     
                
        #finding the constant
        elif "**" not in term and "*" not in term and term != symbol :
            if term.lstrip('-').isdigit():
                c = int(term)
            else:
                try:
            # Try to convert to float
                    c = float(term)
                except ValueError:
            # If it fails, handle as fraction
                    numerator, denominator = map(int,term.split('/'))
                    decimal = Decimal(numerator) / Decimal(denominator)
                    c = float(decimal.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))     
    return [a, b, c]


def solve_quad_no_factor(equation):
    symbol = find_symbol(equation)
    terms = splitting_terms(equation)
    result = []
    
    a, b, c = determine_coefficients(terms, symbol)
    answer = quadratic_formula(a, b, c)
   
    result.append(f"Use quadratic equation with a = {a}, b = {b} and c = {c}")
    if answer == "No real solutions":
        answer = []
        left, right = equation.split('=')
        imaginary_numbers = solve(left, symbol)
        imaginary_numbers_as_strings = [f"x = {num}" for num in imaginary_numbers]
        answer.extend(imaginary_numbers_as_strings)
        result.append(answer)
    else:
        result.append([symbol + " = " + str(answer[0]), symbol + " = " + str(answer[1])])
    return result

def array_factors_coefficient(x):
    results = []
    if x > 0:
        for i in range(1, x+1):
            if x % i == 0:
                results.append([i, int(x/i)])
                results.append([-i, int(-x/i)])
    if x < 0:            
        for i in range(x+1, 0):
            if x % i == 0:
                results.append([i, int(x/i)])
        for i in range(1, -(x+1)):
            if x % i == 0:
                results.append([i, int(x/i)])
    if x == 1:
        results.append([1,1])
    if x == -1:
        results.append([1,-1])
        results.append([-1,1])
             
    return results

def format_solution(solution):
    fraction = Fraction(solution).limit_denominator()
    
    if fraction.denominator == 1:
        return str(fraction.numerator)
    
    return str(fraction)

def generate_equation_and_solution(a, b, d, e, symbol):
    
    
    part1 = f"{a if a != 1 else ''}{symbol}" if a != 0 else ''
    part2 = f" {'+' if d >= 0 else '-'} {abs(d)}" if d != 0 else ''
    part3 = f"{b if b != 1 else ''}{symbol}" if b != 0 else ''
    part4 = f" {'+' if e >= 0 else '-'} {abs(e)}" if e != 0 else ''
    
    if a == -1:
        part1 = f"-{symbol}"
    if b == -1:
        part3 = f"-{symbol}"
    
    equation = f"({part1}{part2})({part3}{part4}) = 0"
    solution_d = f"{symbol} = {format_solution(-d/a)}" if d != 0 else None
    solution_e = f"{symbol} = {format_solution(-e/b)}" if e != 0 else None
    solutions = [sol for sol in [solution_d, solution_e] if sol is not None]

    return [equation, solutions]

            
def unique_solutions(solutions):
    unique_solutions = []
    for solution in solutions:
        if solution not in unique_solutions:
            unique_solutions.append(solution)
    return unique_solutions


def solve_quad_factor(equation):
    symbol = find_symbol(equation)
    terms = splitting_terms(equation)
    A, B, c = determine_coefficients(terms, symbol)

    factors_a = array_factors_coefficient(A)
    factors_c = array_factors_coefficient(c)
    result = []
    solutions = []

    if c == 0:
        solutions.append(f"{symbol} = 0")

        sign = '-' if B < 0 else '+'
        B_abs = abs(B)
        if A == 1:
            new_equation_left = f"{symbol} {sign} {B_abs}"
        else:
            new_equation_left = f"{A}{symbol} {sign} {B_abs}"

        new_equation = new_equation_left + " = 0"
        result.append(f'x({new_equation_left}) = 0')
        second_solution = solve_linear_y_intercept_eq(new_equation)[-1]
        solutions.append(second_solution)
        result.append(solutions)

    else:
        """
        Part below is calculating the right combination for the Factors of A and the factors of C that will be added up to get B 
        a normal factored out equation looks like this: (ax + d)(bx - e)
        so we need a*d = A or the coefficient of x^2
        and we need b*e = C or the constant
        but we also need b*d + a*e = B which is the coefficient to the middle term

        And we also need to take into consideration what is negative and what is positive to be sure we are producing the correct results
        """
        #the factor arrays for a nad c here are written as [[a,n], [b,m]] where a*n = A and ditto for b*m = A
        a, b, d, e = 0, 0, 0, 0
        for factor_a in factors_a:
            for factor_c in factors_c:
                if factor_a[0]*factor_c[1] + factor_a[1]*factor_c[0] == B:
                    a = factor_a[0]
                    b = factor_a[1]
                    d = factor_c[0]
                    e = factor_c[1]
                
                
        
        
        # the factored out equation will look like this when it is returned (ax + d)(bx + e) = 0
        equation, solutions = generate_equation_and_solution(a, b, d, e, symbol)
        result.append(equation)
        
        solutions = unique_solutions(solutions)
        result.append(solutions)

    return result


