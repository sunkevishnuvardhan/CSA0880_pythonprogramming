def inverted_full_pyramid(n):
    for i in range(0, n , - 1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print()
n=int(input("N:"))        
inverted_full_pyramid(n)          