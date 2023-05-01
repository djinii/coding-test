import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    n=int(input())
    result=[]
    cnt=1
    for _ in range(n):
        a,b=map(int,input().split())
        result.append((a,b))
    result.sort()
    s=result[0][1]
    for i in range(1,n):
        if s>result[i][1]:
            s=result[i][1]
            cnt+=1
    print(cnt)