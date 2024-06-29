import math

def count_factors_in_factorial(N):
    factors_count = 0
    if N < 0:
        return 0
    
    for i in range(1, N + 1):
        factors_count += math.floor(N / (5 ** i))
    
    return factors_count

N = int(input("N:"))
num_factors = count_factors_in_factorial(N)
print(f"The number of factors in {N}! is: {num_factors}")
