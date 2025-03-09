a = list(map(int, input().split()))
answer = [1, 1, 2, 2, 2, 8]

for i in range(len(a)) :
    a[i] = answer[i] - a[i]

print(" ".join(map(str, a))) 