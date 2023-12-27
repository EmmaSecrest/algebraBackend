import re
from collections import Counter

def simplify_monomials(term):
    # Count the occurrences of each variable in the term
    variable_counts = Counter(term)

    # If all symbols are the same, return the symbol raised to the power of the count
    if len(variable_counts) == 1:
        variable, count = variable_counts.popitem()
        return f'{variable}^{count}' if count > 1 else variable

    # Otherwise, build the simplified term
    simplified_term = ''
    for variable, count in variable_counts.items():
        simplified_term += f'{variable}^{count}' if count > 1 else variable

    return simplified_term
  

def simplify_polynomials(expression):
    # Split the expression into terms
    terms = expression.split('+')

    # Simplify each term and count the occurrences of each simplified term
    simplified_terms = [simplify_monomials(term) for term in terms if not term.isdigit()]
    term_counts = Counter(simplified_terms)

    # Add up the constants
    constants = sum(int(term) for term in terms if term.isdigit())

    # Combine the terms back into a single expression
    simplified_expression = '+'.join(f'{count if count > 1 else ""}{term}' for term, count in term_counts.items())

    # Add the sum of the constants to the expression
    if constants > 0:
        simplified_expression += f'+{constants}'

    return simplified_expression

