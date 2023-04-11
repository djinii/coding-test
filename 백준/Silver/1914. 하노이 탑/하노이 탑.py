import sys
n=int(sys.stdin.readline())
def hanoi(n,s,m,e):
    if n==1:
        print(s,e)
    else:
        hanoi(n-1,s,e,m)
        hanoi(1,s,m,e)
        hanoi(n-1,m,s,e)
def count(n):
    if n==1:
        k=1
        return k
    else:
        k=2**(n-1)+count(n-1)
        return k
print(count(n))
if n <= 20:
    hanoi(n,1,2,3)