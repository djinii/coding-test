import heapq
import sys
n=int(sys.stdin.readline())
d=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if not d:
            print('0')
        else:
            print(-heapq.heappop(d))
    else:
        heapq.heappush(d,-x)
