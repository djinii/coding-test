import sys
input = sys.stdin.readline
num_str = input()
if(num_str[0] == '0'):
    if(num_str[1]=='x'):
        num = int(num_str[2:-1],16)
    else :
        num = int(num_str[1:-1],8)
    print(num)
else :
    print(int(num_str))