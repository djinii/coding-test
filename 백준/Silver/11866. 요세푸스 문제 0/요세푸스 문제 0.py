from collections import deque
import sys
n, k=map(int,sys.stdin.readline().split())
d=deque()
new_list=[]
for i in range(1,n+1):
    d.append(i)
while d:
    if len(d)==1:
        new_list.append(d.popleft())
    elif len(d)>=k:
        new_list.append(d[k-1])
        d.rotate(len(d)-k+1)
        d.popleft()
    elif len(d)<k:
        for j in range(k-1):
            d.rotate(-1)
        new_list.append(d.popleft())
    
string = '<' + ', '.join(map(str, new_list)) + '>'
print(string)