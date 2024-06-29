a=int(input("Enter N:"))
x=[]
for i in range(a):
    k=int(input("enter the value of N:"))
    x.append(k)
m=sorted(x)
d=m[-2:]    
print(d)