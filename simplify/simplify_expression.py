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
    simplified_terms = []
    constants = 0

    # Split the expression into terms
    terms = re.split('([+-])', expression)

    # Iterate through each term
    for i in range(0, len(terms), 2):
        # Check if the term is a constant
        if terms[i].isdigit() or (terms[i][0] == '-' and terms[i][1:].isdigit()):
            # Handle subtraction
            if i > 0 and terms[i-1] == '-':
                constants -= int(terms[i])
            else:
                constants += int(terms[i])
        else:
            # Simplify the non-constant term and add it to the list
            simplified_term = simplify_monomials(terms[i])
            if simplified_term:
                simplified_terms.append(simplified_term)

    # Count the occurrences of each simplified term
    term_counts = Counter(simplified_terms)

    # Combine the terms back into a single expression
    simplified_expression = '+'.join(f'{count if count > 1 else ""}{term}' for term, count in term_counts.items())

    # Add the sum of the constants to the expression
    if constants != 0:
        if constants > 0:
            simplified_expression += f'+{constants}'
        else:
            simplified_expression += str(constants)  # '-' sign is included in str(constants) if constants < 0

    return simplified_expression