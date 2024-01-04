import re
from collections import Counter

def simplify_monomials(term):
    # Split the term into variables and their powers
    variables_and_powers = re.findall(r'([a-z]\*\*\d+|[a-z])', term)

    # Count the occurrences of each variable in the term
    variable_counts = Counter()
    for vp in variables_and_powers:
        if '**' in vp:
            variable, power = vp.split('**')
            variable_counts[variable] += int(power)
        else:
            variable_counts[vp] += 1

    # If all symbols are the same, return the symbol raised to the power of the count
    if len(variable_counts) == 1:
        variable, count = variable_counts.popitem()
        return f'{variable}**{count}' if count > 1 else variable

    # Otherwise, build the simplified term
    simplified_term = ''
    for variable, count in variable_counts.items():
        simplified_term += f'{variable}**{count}' if count > 1 else f'{variable}'

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
