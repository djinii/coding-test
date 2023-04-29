import sys
s=list(input().split('-'))
r=[]
sm=0
n=0
c=0
for a in s: 
    r.append(a.split('+'))
for q in range(len(r[0])):
    n+=int(r[0][q])
for i in range(1,len(r)):
    
    if len(r[i])>1:
        for j in range(len(r[i])):
            n-=int(r[i][j])
    else:
        b=int(r[i][0])
        n-=b
print(n)