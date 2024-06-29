def inverted_full_pyramid(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        print("")
n = int(input("N:"))
inverted_full_pyramid(n)       