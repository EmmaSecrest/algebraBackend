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
                
       



def solve_quad_no_factor(equation):
    symbol = find_symbol(equation)
    terms = splitting_terms(equation)
    result = []
    
    
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
            
    answer = quadratic_formula(a, b, c)
   
    result.append(f"Use quadratic equation with a = {a}, b = {b} and c = {c}")
    if answer == "No real solutions":
        result.append(answer)
    else:
        result.append([symbol + " = " + str(answer[0]), symbol + " = " + str(answer[1])])
    return result
            
            
            
    
