import sys
n=int(sys.stdin.readline())
li=[0]*(n+1)
li[0]=0
li[1]=1

def fibo(n):
    if li[n]==0 and n>1:
        li[n]=fibo(n-1)+fibo(n-2)
    return li[n]

print(fibo(n))