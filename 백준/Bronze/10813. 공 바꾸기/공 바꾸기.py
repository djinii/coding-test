n, m = map(int, input().split())
baskets = [i+1 for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    c = baskets[a-1]
    baskets[a-1] = baskets[b-1]
    baskets[b-1] = c

print(' '.join(map(str, baskets)))