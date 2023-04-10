import sys
import math
a, b, v=map(int, sys.stdin.readline().split())
l=v-a #
cnt=1
if l <=0:
    pass
else:
    up=a-b
    cnt+=math.ceil(l/up)
print(cnt)