outer_lst = []
for i in range(9) :
    inner_lst = list(map(int, input().split()))
    outer_lst.append(inner_lst)
m = 0
x = 0
y = 0
for j in range(9) :
    for q in range(9) :
        if m <= outer_lst[j][q] :
            m = outer_lst[j][q]
            x = j+1
            y = q+1
print(m)
print(x, y)