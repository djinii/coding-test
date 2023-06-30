tests = int(input())

for i in range(tests):
    sum = 0
    avg = 0
    cnt = 0 
    high = 0 

    std_li = list(map(int, input().split()))
    for j in range(1, std_li[0]+1):
        sum += std_li[j]
    avg = sum / std_li[0]
    for q in range(1, std_li[0]+1):
        if (std_li[q] > avg):
            cnt += 1
    print(f"{((cnt*100) / std_li[0]):.3f}%")