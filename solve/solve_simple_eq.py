from sympy import symbols, degree, Eq, solve, sympify
from simplify.simplify_expression import simplify_polynomials
import re

def set_up_to_solve(equation):
    left, right = equation.split('=')
    # Simplify the left and right sides of the equation
    left = simplify_polynomials(left)
    right = simplify_polynomials(right)
    # Subtract the right side from the left side and simplify the result
    simplified = simplify_polynomials(f'{left} - ({right})')
    return f'{simplified} = 0'

def find_degree(equation):
    x = symbols('x')
    left,right = equation.split('=')
    left_side = sympify(left)
    highest_degree = degree(left_side, gen=x)
    
    return highest_degree
   
    


def solve_simple_eq(equation):
    new_eq = set_up_to_solve(equation)
    #determine the degree of the equation
    print("new_eq",new_eq)
    degree = find_degree(new_eq)
    left,right = new_eq.split('=')
    
    result = []
    if degree == 1:
        split = re.split(r'[\+-]', left)
        print("split eq",split)
        print("length of first element",len(split[0]))
        length_of_first_element = len(split[0].replace(" ", ""))
        if length_of_first_element == 1:
            opposite = - int(split[1])
            solution =  split[0] + "= " + split[1].replace(" ", "")
            result = ["adding " + str(opposite) + " to both sides of the equation" ,solution]
        if length_of_first_element > 1:
            
            opposite = - int(split[1])
            split_first_part = split[0].split("*")
            variable = split_first_part[1].replace(" ", "")
            coefficient = split_first_part[0].replace(" ", "")
            final = int(opposite / int(coefficient)) if opposite % int(coefficient) == 0 else opposite / int(coefficient)
            result_pt1 = "moving " + str(opposite) + " to the left side of the equation"
            result_pt2 = "adding " + str(opposite) + " from both sides"
            result_pt3 = "dividing each side by " + str(coefficient)
            result_pt4 = variable + " = " + str(final) 
            result = [result_pt1,result_pt2,result_pt3,result_pt4]
                
    return result
     
         
    

