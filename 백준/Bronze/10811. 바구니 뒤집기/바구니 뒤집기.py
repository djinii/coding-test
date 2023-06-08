import sys
input = sys.stdin.readline
n, m = map(int,input().split())
basket01=[]
basket02=[]

for i in range(1, n+1):
    basket01.append(i)
    basket02.append(i)

for _ in range(m):
    start, end = map(int,input().split())
    nm = 0
    start -= 1
    end -= 1
    for _ in range(start, end+1):
        basket01[start+nm] = basket02[end-nm]
        nm += 1

    for q in range(n):
        basket02[q] = basket01[q]

print(' '.join(map(str, basket02)))