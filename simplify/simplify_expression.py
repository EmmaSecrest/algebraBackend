import re
from collections import defaultdict

def simplify_monomials(expression):
    variable_counts = defaultdict(int)
    coefficient = 1

    for cv in re.findall('(-?\d*)?([a-z]*)', expression):
        if cv[1]:
            for variable in cv[1]:
                variable_counts[variable] += int(cv[0]) if cv[0] else 1
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
    simplified_monomials = [simplify_monomials(monomial) if monomial not in ['+', '-'] else monomial for monomial in monomials]

    # Group and count the 'x' terms
    x_counts = defaultdict(int)
    for i, monomial in enumerate(simplified_monomials):
        if 'x' in monomial:
            variable = monomial.split('x')[1]
            print("variable", variable)
            count = x_counts[variable]
            simplified_monomials[i] = f'{count if count != 1 else ""}x{variable}'
            print("simplified_monomials[i]", simplified_monomials[i])

    # Replace the 'x' terms in the simplified monomials with their counts
    for i, monomial in enumerate(simplified_monomials):
        if 'x' in monomial:
           count = x_counts[variable]
           simplified_monomials[i] = f'{count if count != 0 else ""}x{variable}'

    # Join the simplified monomials with '+'
    return ''.join(simplified_monomials)