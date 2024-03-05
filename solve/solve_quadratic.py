from simplify.simplify_expression import simplify_polynomials
import re
import math

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
    
    # need to go through the factors of a and c to find the combination of factors that add up to b        
    # after found the a = factor_a[x][0] , b = factor_a[x][1], d = factor_c[y][0], e = factor_c[y][1] where x and y are the indexes of the factors that work
    # B = bd +ae
    for i in range(len(factors_a)):
        for j in range(len(factors_c)):
            if factors_a[i][0] * factors_c[j][1] + factors_a[i][1] * factors_c[j][0] == B:
                a = factors_a[i][0]
                b = factors_a[i][1]
                d = factors_c[j][0]
                e = factors_c[j][1]
                break

    solutions = []
    # result.append(f"({a}{symbol} + {d})({b}{symbol} + {e}) = 0")
   
    if a == 1 and b ==1:
        if d > 0 and e > 0:
            result.append(f"({symbol} + {d})({symbol} + {e}) = 0")
        if d < 0 and e < 0:
            result.append(f"({symbol} - {d})({symbol} - {e}) = 0")
        if d > 0 and e < 0:
            result.append(f"({symbol} + {d})({symbol} - {e}) = 0")
        if d < 0 and e > 0:
            result.append(f"({symbol} - {d})({symbol} + {e}) = 0")        
        
        
        if d>0:
          solutions.append(f"{symbol} = -{d}")
        elif d<0:
          solutions.append(f"{symbol} = {abs(d)}")
        if e>0:
            solutions.append(f"{symbol} = -{e}")
        elif e<0:
            solutions.append(f"{symbol} = {abs(e)}")
        
        result.append(solutions)  
    
    
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
        
        result.append(solutions)     
        
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
        
        result.append(solutions)        
    
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
        