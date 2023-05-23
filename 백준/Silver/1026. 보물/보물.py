import sys
input=sys.stdin.readline
n = int(input())
result = 0
list_a  = list(map(int,sys.stdin.readline().split()))[:n]
list_b  = list(map(int,sys.stdin.readline().split()))[:n]

list_a.sort()
list_b.sort(reverse=True)

for i in range(n):
    result += list_a[i] * list_b[i]

print(result)