def sum_multiples_of_3_and_5(N):
    sum_multiples = 0
    for num in range(N):
        if num % 3 == 0 or num % 5 == 0:
            sum_multiples += num
    return sum_multiples
N = int(input("N:"))
result = sum_multiples_of_3_and_5(N)
print(f"The sum of multiples of 3 and 5 below {N} is: {result}")
