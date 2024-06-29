n="my boy is handsome"
s=[]
words=n.split()
for word in words:
    s.append(word)
k=s[::-1]
for i in k:
    print("".join(i),end=" ")