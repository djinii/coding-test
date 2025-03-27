a, b = map(int, input().split())
a1 = int(str(a)[::-1])
b1 = int(str(b)[::-1])


print(int(str(a1+b1)[::-1]))