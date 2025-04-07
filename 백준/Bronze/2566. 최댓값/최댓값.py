big_lst = []
for i in range(9):
    lst = list(map(int, input().split()))
    big_lst.append(lst)

m = -1
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if big_lst[i][j] > m:
            m = big_lst[i][j]
            x = i
            y = j

print(m)
print(x+1, y+1)
