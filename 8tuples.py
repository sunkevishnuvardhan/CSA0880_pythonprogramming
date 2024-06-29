def create_tuples_with_squares(n):
    # Using list comprehension to create a list of tuples
    tuples_list = [(num, num**2) for num in range(1, n+1)]
    return tuples_list

n = int(input("N:"))
result = create_tuples_with_squares(n)
print(result)
