import sys
input = sys.stdin.readline

num = int(input())
result_li=[]

for i in range(1, num): 
    nums = [int(n) for n in str(i)] 
    sum = i
    for j in range(len(nums)):
        sum += nums[j]
    if(sum == num):
        result_li.append(i)
if(len(result_li) == 0):
    print('0')
else:
    print(min(result_li))