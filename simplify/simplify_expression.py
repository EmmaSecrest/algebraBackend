import re
from collections import defaultdict
from sympy import simplify

import re

def simplify_monomials(monomial):
    # Split the monomial into variables and their counts
    variable_counts = re.findall(r'([a-z]\*\*[\d]+|[a-z])', monomial)

    # Count the variables
    counts = {}
    for variable in variable_counts:
        if '**' in variable:
            var, count = variable.split('**')
            counts[var] = counts.get(var, 0) + int(count)
        else:
            counts[variable] = counts.get(variable, 0) + 1

    # Build the simplified monomial
    simplified = ''.join(f'{var}**{count}' if count > 1 else var for var, count in counts.items())

    return simplified

def simplify_polynomials(expression):
    # Use sympy's simplify function to simplify the expression
    simplified = simplify(expression)
    return str(simplified)