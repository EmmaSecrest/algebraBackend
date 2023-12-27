from sympy import simplify

def simplify_monomials(expression):
    expression = ''.join(sorted(expression))
    
    result = ''
    count = 1
    for i in range(1, len(expression)):
        if expression[i] == expression[i - 1]:
            count += 1
        else:
            result += expression[i - 1] + ('^' + str(count) if count > 1 else '')
            count = 1
    result += expression[-1] + ('^' + str(count) if count > 1 else '')
    return result
    