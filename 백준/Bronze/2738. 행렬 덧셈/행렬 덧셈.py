n, m = map(int, input().split())
nums = []
result = []

for i in range(n * 2):
    nums.append(list(map(int, input().split())))

for j in range(n):
    tem = []
    for q in range(m):
        num = nums[j][q] + nums[j + n][q]
        tem.append(num)
    result.append(tem)

for row in result:
    print(" ".join(map(str, row)))
