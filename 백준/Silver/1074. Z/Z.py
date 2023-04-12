n,r,c = map(int,input().split())
def a(n,r,c):
    if n==0:
        return 0
    else:
        return 4**(n-1) * (2*(r//2**(n-1))+(c//2**(n-1))) + a(n-1,r%(2**(n-1)),c%(2**(n-1)))
print(a(n,r,c))