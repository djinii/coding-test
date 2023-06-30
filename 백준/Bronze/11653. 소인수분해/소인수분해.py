import sys
input = sys.stdin.readline

num = int(input())
i = 2

while(True):
    if(num == 1):
        break
    if(num%i != 0):
        i += 1
    else :
        num = num // i
        print(i)