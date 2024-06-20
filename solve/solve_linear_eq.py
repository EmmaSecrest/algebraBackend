from sympy import symbols, degree, Eq, solve, sympify
from simplify.simplify_expression import simplify_polynomials
import re

#needs to be in y intercept form
def set_up_to_solve(equation):
    left, right = equation.split('=')
    # Simplify the left and right sides of the equation
    left = simplify_polynomials(left)
    right = simplify_polynomials(right)
    result = left + " = " + right
    return result
        

def find_symbol(equation):
    # This regular expression matches any non-numeric and non-operator character
    matches = re.findall(r'[^\d\+\-\*\/\=\s]', equation)
    # Filter out any empty strings
    symbols = [match for match in matches if match]
    return symbols[0] if symbols else None



   
def solve_linear_y_intercept_eq(equation):
    new_eq = set_up_to_solve(equation)
    left,right = new_eq.split('=')
    result = []
    
    if " - " in left:
        left = left.replace(" - ", " + -")
   
    split = left.split("+")
    length_of_first_element = len(split[0].replace(" ", ""))
    
    #if the first element has no coefficient
    if length_of_first_element == 1:
        number_to_add = - int(split[1])
        answer = int(right)+number_to_add
        solution =  split[0] + "= " + str(answer)
        result = ["adding " + str(number_to_add) + " to both sides of the equation" ,solution]
    
    #if the first element has a coefficient
    if length_of_first_element > 1:
        split_first_element = re.split(r'[\*]', split[0])
        coefficient = int(split_first_element[0].replace(" ", ""))            
        if len(split) == 1:
            answer = int(right) / coefficient
            solution = split_first_element[1] + "= " + str(answer)
            result = ["dividing each side of the equation by " + str(coefficient) ,solution]
        
        elif len(split) >= 2 :
            constant = int(split[1].replace(" ", ""))
            answer_top = int(right) + (-constant)
            answer = answer_top / coefficient
            solution = split_first_element[1] + "= " + str(answer)
            result = ["adding " + str(-constant) + " to both sides of the equation" , "dividing each side of the equation by " + str(coefficient),solution]
        

    return result
     
         
    

