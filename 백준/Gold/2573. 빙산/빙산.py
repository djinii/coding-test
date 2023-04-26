from collections import deque
import sys
from itertools import chain
input=sys.stdin.readline
n,m=map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def melting(ice):
    n_ice=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j]!=0:
                cnt = 0
                for k in range(4): 
                    ni=i+dx[k]
                    nj=j+dy[k]
                    if ice[ni][nj]==0:
                        cnt+=1
                n_ice[i][j]=max(ice[i][j]-cnt, 0) #min이 0이다, 음수불가
    return n_ice

def checking(ice):
    visited=[[False]*m for _ in range(n)]
    q=deque()
    cnt = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice[i][j] != 0 and not visited[i][j]:
                q.append([i, j])
                visited[i][j]=True
                while q:
                    x, y =q.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if not visited[nx][ny] and ice[nx][ny] != 0:
                            visited[nx][ny] = True
                            q.append([nx, ny])
                cnt += 1
    return cnt               
time=0
def sol(ice):
    global time
    if sum(chain(*ice)) == 0:
        print(0)
        return
    ice = melting(ice)
    cnt = checking(ice)
    time += 1
    if cnt>1:
        print(time)
        return
    sol(ice)

sol(ice)