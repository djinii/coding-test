l=[]
for i in range(9):
    a=int(input())
    l.append(a)
m=max(l)
print(m)
print(l.index(m)+1)