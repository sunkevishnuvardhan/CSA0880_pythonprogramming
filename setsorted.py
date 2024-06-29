n=int(input("Enter:"))
list1=[]
list2=[]
for i in range(n):
    k=int(input("Enter the N:"))
    list1.append(k)   
m=int(input("Enter:"))
for j in range(m):
    l=int(input("Enter the N:"))
    list2.append(l)
print(list1+list2)