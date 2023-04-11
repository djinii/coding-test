import sys
n=int(sys.stdin.readline())

def f(n):
    r=1
    if n>1:
        r=n*f(n-1)
    return r
print(f(n))