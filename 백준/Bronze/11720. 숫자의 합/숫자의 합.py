import sys
input = sys.stdin.readline
num = int(input())
str = input()
sum = 0
num_li=[]
for i in range(num):
    num_li.append(int(str[i]))
    sum += num_li[i]
print(sum)
