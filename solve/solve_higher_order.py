def solve_synthetic_division(equation):
    pass

def array_factors_coefficient_list(x):
    results = set()
    for i in range(1, abs(x) + 1):
        if x % i == 0:
            results.add(i)
            results.add(-i)
            results.add(x // i)
            results.add(-x // i)
    return list(results)