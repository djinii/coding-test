import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

lo = min(m, n)
hi = max(m, n)

prime = [True] * (hi + 1)
if hi >= 0: prime[0] = False
if hi >= 1: prime[1] = False

for i in range(2, int(hi**0.5) + 1):
    if prime[i]:
        for j in range(i*i, hi + 1, i):
            prime[j] = False

result = [i for i in range(max(2, lo), hi + 1) if prime[i]]

if not result:
    print(-1)
else:
    print(sum(result))
    print(result[0])
