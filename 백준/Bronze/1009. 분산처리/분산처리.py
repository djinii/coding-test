n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        b = (b % 4) + 4
        print((a ** b) % 10)
