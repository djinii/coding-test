import sys
t = int(input())
num_list = []
for i in range(t):
    num = list(input().split(','))
    num_list.append(num)
    print(int(num_list[i][0]) + int(num_list[i][1]))