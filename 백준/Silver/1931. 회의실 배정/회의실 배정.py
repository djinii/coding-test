import sys
n=int(sys.stdin.readline())
time=[]
cnt=1
for _ in range(n):

    start,end=map(int, sys.stdin.readline().split())
    time.append((start,end))
time.sort(key=lambda x:(x[1], x[0]))
a=time[0][1]
for i in range(1,n):
    if a<=time[i][0]:
        a=time[i][1]
        cnt+=1
print(cnt)