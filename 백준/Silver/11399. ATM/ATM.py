import sys
n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
total=[]
s = times[0]
total.append(s)
for i in range(1, n):
    if (n > 1):
        s += times[i]
        total.append(s)
result = 0
for j in range(n):
    result+=total[j]
print(result)