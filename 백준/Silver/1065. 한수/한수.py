import sys
N=sys.stdin.readline()

# print(type(N)):타입 알아내는 방법
if int(N)<100:
    print(N)
else:
    cnt=99
    for i in range(100,int(N) +1):
        li=list(map(int,str(i)))
        a=li[0]-li[1]
        b=li[1]-li[2]
        if a==b:
            cnt+=1
    print(cnt)