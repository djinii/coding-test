a, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

for i in range(a - 1):
    swapped = False
    for j in range(a - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            cnt += 1
            swapped = True
            if cnt == k:
                print(*lst)
                exit()
    if not swapped:
        break

print(-1)
