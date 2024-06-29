def full_pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()
n = int(input("N:"))
full_pyramid(n)
def reverse_diamond(n):
    for i in range(n,0, -1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()       
reverse_diamond(n)  