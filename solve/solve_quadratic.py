from simplify.simplify_expression import simplify_polynomials
import re
import math
from solve.solve_linear_eq import solve_linear_y_intercept_eq

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

def set_up_to_solve_quadratic(equation):
    left, right = equation.split('=')
    left = simplify_polynomials(left)
    right = simplify_polynomials(right)
    # Distribute the negation across the right side
    right = distribute_negation(right)
    result = left + right
    result = simplify_polynomials(result)
    result = result + " = 0"
    return result

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
        part_1 = math.sqrt(determinate)
        part_2 = 2*a
        solution_1 = (-b + part_1) / part_2
        solution_2 = (-b - part_1) / part_2
        solutions = [solution_1, solution_2]
        
        for i in range(len(solutions)):
            if str(solutions[i]).endswith('.0'):
                solutions[i] = int(solutions[i])
            else:
                solutions[i] = round(solutions[i], 2)
                
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
                
                a = int(second_split[0])
            elif split[0] == symbol:
                a = 1    
            else:
                print("split 0", split[0])
        #finding the coefficient of b
        elif symbol in term and "*" in term and "**2" not in term or term == symbol:
            if term == symbol:
                b = 1
            else:
                split = term.split("*")
                b = int(split[0])
            
        #finding the constant
        elif "**" not in term and "*" not in term and term != symbol:
            c = int(term)
            
    return [a, b, c]


def solve_quad_no_factor(equation):
    symbol = find_symbol(equation)
    terms = splitting_terms(equation)
    result = []
    
    a, b, c = determine_coefficients(terms, symbol)
            
    answer = quadratic_formula(a, b, c)
   
    result.append(f"Use quadratic equation with a = {a}, b = {b} and c = {c}")
    if answer == "No real solutions":
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


            

def solve_quad_factor(equation):
    symbol = find_symbol(equation)
    terms = splitting_terms(equation)
    A, B, c = determine_coefficients(terms, symbol)      
    
    factors_a = array_factors_coefficient(A)
    factors_c = array_factors_coefficient(c)
    a = 0
    b = 0
    d = 0
    e = 0
    result = []
    solutions = []
    
    
    if c == 0:
        solutions.append(f"{symbol} = 0")
        
        if B < 0 and A != 1:
            new_equation_left = f"{A}{symbol} - {abs(B)}"
        elif A == 1 and B > 0:
            new_equation_left= f"{symbol} + {B}"
        elif A == 1 and B < 0:
            new_equation_left = f"{symbol} - {abs(B)}"
        else:
            new_equation_left = f"{A}{symbol} + {B}" 
        
        new_equation = new_equation_left + " = 0"
        print("new equation: ", new_equation)
        result.append(f'x({new_equation_left}) = 0')
        second_solution = solve_linear_y_intercept_eq(new_equation)[-1]
        print("solve linear eq: " ,solve_linear_y_intercept_eq(new_equation))
        solutions.append(second_solution)
        

    """ 
    Part below is calculating the right combination for the the Factors of A and the factors of C that will be added up to get B 
    a normal factored out equation looks like this: (ax + b)(dx - e)
    so we need a*d = A or the coefficient of x^2
    and we need b*e = C or the constant
    but we also need b*d + a*c = B which is the coefficient to the middle term
    
    And we also need to take into consideration what is negative and what is positive to be sure we are producing the correct results
    """
    
    
    signs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    
    for i in range(len(factors_a)):
        for j in range(len(factors_c)):
            for sign_a, sign_c in signs:
                
                if (sign_a * factors_a[i][0] * factors_c[j][1] + sign_c * factors_a[i][1] * factors_c[j][0]) == B:
                    a = factors_a[i][0]
                    b = factors_a[i][1]
                    d = sign_a*factors_c[j][0]
                    e = sign_c*factors_c[j][1]
                    
                    break
               
                
  
    if a == 1 and b ==1:
        if d > 0 and e > 0:
            result.append(f"({symbol} + {d})({symbol} + {e}) = 0")
        if d < 0 and e < 0:
            result.append(f"({symbol} - {abs(d)})({symbol} - {abs(e)}) = 0")
        if d > 0 and e < 0:
            result.append(f"({symbol} + {d})({symbol} - {abs(e)}) = 0")
        if d < 0 and e > 0:
            result.append(f"({symbol} - {abs(d)})({symbol} + {e}) = 0")        
        
        
        if d>0:
          solutions.append(f"{symbol} = -{d}")
        elif d<0:
          solutions.append(f"{symbol} = {abs(d)}")
        if e>0:
            solutions.append(f"{symbol} = -{e}")
        elif e<0:
            solutions.append(f"{symbol} = {abs(e)}")
        
        
    
    
    elif a == 1:
        
        if d > 0 and e > 0:
            result.append(f"({symbol} + {d})({b}{symbol} + {e}) = 0")
        elif e < 0 and d < 0:
            result.append(f"({symbol} - {abs(d)})({b}{symbol} - {abs(e)}) = 0")
        elif d > 0 and e < 0:
            result.append(f"({symbol} + {abs(d)})({b}{symbol} - {abs(e)}) = 0")
        elif e > 0 and d < 0:
            result.append(f"({symbol} - {abs(d)})({b}{symbol} + {abs(e)}) = 0")
        
        if d>0:
          solutions.append(f"{symbol} = -{d}")
        elif d<0:
          solutions.append(f"{symbol} = {abs(d)}")
          
        if b > 0 and e > 0:
            solutions.append(f'{symbol} = -{e}/{b}')
        elif e < 0 and b < 0:
            solutions.append(f'{symbol} = -{e}/{b}')
        elif b > 0 and e < 0:
            solutions.append(f'{symbol} = {abs(e)}/{abs(b)}')
        elif b < 0 and e > 0:
            solutions.append(f'{symbol} = {abs(e)}/{abs(b)}')
        
            
        
    elif b == 1:
        
        if d > 0 and e > 0:
            result.append(f"({a}{symbol} + {d})({symbol} + {e}) = 0")
        elif e < 0 and d < 0:
            result.append(f"({a}{symbol} - {abs(d)})({symbol} - {abs(e)}) = 0")
        elif d > 0 and e < 0:
            result.append(f"({a}{symbol} + {abs(d)})({symbol} - {abs(e)}) = 0")
        elif e < 0 and d > 0:
            result.append(f"({a}{symbol} - {abs(d)})({symbol} + {abs(e)}) = 0")
        
        if d > 0 and a > 0:
            solutions.append(f'{symbol} = -{d}/{a}')
        elif d < 0 and a < 0:
            solutions.append(f'{symbol} = -{d}/{a}')
        elif d > 0 and a < 0:
            solutions.append(f'{symbol} = {abs(d)}/{abs(a)}')
        elif d < 0 and a > 0:
            solutions.append(f'{symbol} = {abs(d)}/{abs(a)}')    
            
        if e > 0:
            solutions.append(f"{symbol} = -{e}")
        elif e < 0:
            solutions.append(f"{symbol} = {abs(e)}")
        
              
    
    else:
        
        if d > 0 and e > 0:
            result.append(f"({a}{symbol} + {d})({b}{symbol} + {e}) = 0")
        elif e < 0 and d < 0:
            result.append(f"({a}{symbol} - {abs(d)})({b}{symbol} - {abs(e)}) = 0")
        elif d > 0 and e < 0:
            result.append(f"({a}{symbol} + {abs(d)})({b}{symbol} - {abs(e)}) = 0")
        elif d < 0 and e > 0:
            result.append(f"({a}{symbol} - {abs(d)})({b}{symbol} + {abs(e)}) = 0")
        
        if d > 0 and a > 0:
            solutions.append(f'{symbol} = -{d}/{a}')
        elif d < 0 and a < 0:
            solutions.append(f'{symbol} = -{d}/{a}')
        elif d > 0 and a < 0:
            solutions.append(f'{symbol} = {abs(d)}/{abs(a)}')
        elif d < 0 and a > 0:
            solutions.append(f'{symbol} = {abs(d)}/{abs(a)}')
            
        if b > 0 and e > 0:
            solutions.append(f'{symbol} = -{e}/{b}')
        elif e < 0 and b < 0:
            solutions.append(f'{symbol} = -{e}/{b}')
        elif b > 0 and e < 0:
            solutions.append(f'{symbol} = {abs(e)}/{abs(b)}')
        elif b < 0 and e > 0:
            solutions.append(f'{symbol} = {abs(e)}/{abs(b)}')
            
    result.append(solutions) 
    
    return result
        