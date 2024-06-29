def sum_multiples_3_and_5(n):
    sum_multiples = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            sum_multiples += num
    return sum_multiples
n = int(input("N:"))
result = sum_multiples_3_and_5(n)
print(f"The sum of multiples of 3 and 5 below {n} is: {result}")
