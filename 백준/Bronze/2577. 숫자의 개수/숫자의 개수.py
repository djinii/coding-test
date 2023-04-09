import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())

mul=str(a*b*c) 

for j in range(10):
    count=0
    for i in range(len(mul)):
        n=int(mul[i])
        if n==j:
            count=count+1
    print(count)