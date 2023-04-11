import sys
t=int(sys.stdin.readline())
li=[]
for i in range(t):
    n=int(sys.stdin.readline())
    li.append(n)
li.sort()
for j in range(len(li)):
    print(li[j])