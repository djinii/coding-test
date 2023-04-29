import sys
n = int(sys.stdin.readline())
a, b = 1, 0
for _ in range(n):
    a, b = (a+b)%15746, a
print(a)