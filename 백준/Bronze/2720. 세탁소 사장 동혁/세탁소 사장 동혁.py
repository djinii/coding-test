t = int(input())
for i in range(t) :
    li =[0] * 4
    c = int(input())
    li[0] = c // 25
    c %= 25
    li[1] = c // 10
    c %= 10
    li[2] = c // 5
    c %= 5
    li[3] = c // 1
    print(*li)