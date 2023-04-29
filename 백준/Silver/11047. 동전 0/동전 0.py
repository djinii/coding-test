import sys
input=sys.stdin.readline
n,k=map(int,input().split())
currency=[]*(n+1)
cnt=0
for i in range(n):
    a=int(input())
    currency.append(a)
m=k
for i in range(1,n+1):
    if m==0:
        break
    if currency[n-i]<=m:
        cnt+=m//currency[n-i]
        m=m%currency[n-i]
print(cnt)