import sys
n = int(sys.stdin.readline())
s_list=[]
for _ in range(n):
    r, s = map(str, sys.stdin.readline().split())
    r = int(r)
    for i in range(len(s)):
        for j in range(r):
            print(s[i],end='')
    print()