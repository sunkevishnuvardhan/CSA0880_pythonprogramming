def difference_sum_of_squares_square_of_sum(n):
    # Compute sum of squares
    sum_of_squares = sum(i**2 for i in range(1, n+1))

    # Compute square of sum
    sum_of_numbers = sum(range(1, n+1))
    square_of_sum = sum_of_numbers ** 2

    # Compute the difference
    difference = square_of_sum - sum_of_squares

    return difference

# Example usage:
n = 10
result = difference_sum_of_squares_square_of_sum(n)
print(f"Difference between sum of squares and square of sum for first {n} natural numbers: {result}")
