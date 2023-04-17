import sys
N=int(sys.stdin.readline())
sticks=[]

cnt=1
for i in range(N):
    stick=int(sys.stdin.readline())
    sticks.append(stick)
    
now=sticks[-1]
for j in range(len(sticks)-1): 
    sticks.pop()
    if now<sticks[-1]:
        cnt+=1
        now=sticks[-1]
        
print(cnt)