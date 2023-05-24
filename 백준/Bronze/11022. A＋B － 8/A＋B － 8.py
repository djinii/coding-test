import sys
input = sys.stdin.readline
test_n = int(input())
for i in range(test_n):
    a, b=map(int, input().split())
    print('Case #' + str((i+1)) + ': '+str(a)+' + '+str(b) +' = ' + str(a+b))