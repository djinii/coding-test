n = int(input())

lst = list(map(int,input().split()))

sn = int(input())

cnt = 0

for i in range(n):

    if lst[i] == sn:

        cnt += 1

print(cnt)