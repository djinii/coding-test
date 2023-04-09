import sys
a, b=map(str,sys.stdin.readline().split())
n =[]
m=[]
for i in range(1,4):
    n.append(a[-i])
    m.append(b[-i])
n=int(('').join(n))
m=int(('').join(m))
if n>m: 
    print(n)    
else:
    print(m)