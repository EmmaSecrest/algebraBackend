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
    print("equation in find symbol",equation)
    matches = re.findall(r'[^\d\+\-\*\/\=\s]', equation)
    # Filter out any empty strings
    symbols = [match for match in matches if match]
    return symbols[0] if symbols else None


def find_degree(equation, symbol):
    s = symbols(symbol)
    left, right = equation.split('=')
    left_side = sympify(left)
    highest_degree = degree(left_side, gen=s)
    
    return highest_degree
   
    


def solve_simple_eq(equation):
    new_eq = set_up_to_solve(equation)
    #determine the degree of the equation
    left,right = new_eq.split('=')
    print ("left",left)
    print("right",right)
    print("new_eq",new_eq)
    symbol = find_symbol(left)
    degree = find_degree(new_eq,symbol)
    
    

    
    result = []
    if degree == 1:
        split = re.split(r'[\+-]', left)
        print("split eq",split)
        print("length of first element",len(split[0]))
        length_of_first_element = len(split[0].replace(" ", ""))
        if length_of_first_element == 1:
            number_to_add = - int(split[1])
            answer = int(right)+number_to_add
            solution =  split[0] + "= " + str(answer)
            result = ["adding " + str(number_to_add) + " to both sides of the equation" ,solution]
        if length_of_first_element > 1:
            pass
            # opposite = - int(split[1])
            # split_first_part = split[0].split("*")
            # variable = split_first_part[1].replace(" ", "")
            # coefficient = split_first_part[0].replace(" ", "")
            # final = int(opposite / int(coefficient)) if opposite % int(coefficient) == 0 else opposite / int(coefficient)
            # result_pt1 = "moving everything to the left side of the equation"
            # result_pt2 = "adding " + str(opposite) + " from both sides"
            # result_pt3 = "dividing each side by " + str(coefficient)
            # result_pt4 = variable + " = " + str(final) 
            # result = [result_pt1,result_pt2,result_pt3,result_pt4]
                
    return result
     
         
    

