import sys
w, h=map(int, sys.stdin.readline().split())
li01=[0,w]
li02=[0,h]
li03=[]
li04=[]
c=int(sys.stdin.readline())

for i in range(c):
    a, b=map(int,sys.stdin.readline().split())
    if a==0:
        li02.append(b)
    else:
        li01.append(b)
    li01.sort()
    li02.sort()
for j in range(len(li02)-1):
    li04.append(abs((li02[j])-(li02[j+1])))

for x in range(len(li01)-1):
    li03.append(abs(li01[x]-li01[x+1]))

print(max(li04)*max(li03))

    
