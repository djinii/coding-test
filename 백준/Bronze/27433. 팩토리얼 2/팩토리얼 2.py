import sys
input=sys.stdin.readline
n=int(input())
result=1
for i in range(1, n+1):
    if n>1:
        result=result*i
    else:
        result=result*1
print(result)