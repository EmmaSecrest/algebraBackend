import re
from collections import defaultdict

def simplify_monomials(expression):
    variable_counts = defaultdict(int)
    coefficient = 1

    for cv in re.findall('(-?\d*)?([a-z])', expression):
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
    # Split the input expression into monomials
    monomials = re.split(r'([+-])', expression)

    # Simplify each monomial using the simplify_monomials function
    simplified_monomials = [simplify_monomials(monomial) for monomial in monomials]

    # Join the simplified monomials back into a single expression
    simplified_expression = ''.join(simplified_monomials)

    # Remove leading '+' if present
    if simplified_expression.startswith('+'):
        simplified_expression = simplified_expression[1:]

    return simplified_expression
