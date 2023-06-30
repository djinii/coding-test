import sys
import re
input = sys.stdin.readline

str_len = input()
str = input()
s = 0
numbers = re.findall(r'\d+', str)

for i in range(len(numbers)):
    s += int(numbers[i])

print(s)