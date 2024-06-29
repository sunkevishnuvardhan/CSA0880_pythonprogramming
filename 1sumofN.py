def sum_of_series(N):
    total_sum = 0
    current_term = 12
    
    for i in range(1, N + 1):
        total_sum += current_term
        current_term += 10 + i 
    
    return total_sum

N = int(input("N:"))
result = sum_of_series(N)
print(f"For N = {N}, the sum of the series is: {result}")
