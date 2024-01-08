import re
from collections import defaultdict

def simplify_monomials(term):
    variable_counts = defaultdict(int)
    coefficient = 1

    for cv in re.findall('(-?\d*)?([a-z])', term):
        if cv[1]:
            variable_counts[cv[1]] += int(cv[0]) if cv[0] else 1
        elif cv[0]:
            coefficient *= int(cv[0])

    if len(variable_counts) == 1:
        variable, count = variable_counts.popitem()
        return f'{coefficient}{variable}**{count}' if count > 1 else f'{coefficient}{variable}'
    elif len(variable_counts) > 1:
        simplified_term = ''.join(f'{variable}**{count}' if count > 1 else f'{variable}' for variable, count in variable_counts.items())
        return f'{coefficient}{simplified_term}' if coefficient != 1 else simplified_term
    else:
        return str(coefficient)

def simplify_polynomials(expression):
    # Split the expression into terms
    terms = re.split('([+-])', expression)
    # Initialize a dictionary to hold the coefficients of each term
    coefficients = defaultdict(int)

    # Iterate over the terms
    for i in range(0, len(terms), 2):
        # Simplify the current term
        simplified_term = simplify_monomials(terms[i])
        if simplified_term:
            # Determine the coefficient of the current term
            coefficient = int(terms[i - 1] + '1') if i > 0 and terms[i - 1] == '-' else 1
            # Add the coefficient to the total for this term
            coefficients[simplified_term] += coefficient

    # Sort the dictionary items based on variable names
    sorted_coefficients = sorted(coefficients.items(), key=lambda x: x[0])

    # Combine the terms back into a single expression
    simplified_expression = '+'.join(f'{"" if count == 1 else count}{term}' for term, count in sorted_coefficients if count != 0)
    # Replace '+-' with '-' for subtraction
    simplified_expression = simplified_expression.replace('+-', '-')
    return simplified_expression


