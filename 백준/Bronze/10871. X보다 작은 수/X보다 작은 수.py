s=list()
n, x=map(int, input().split())
nums=list(map(int,input().split()))
for num in nums:
    if num<x:
        s.append(str(num))
    result=' '.join(s)
print(result)