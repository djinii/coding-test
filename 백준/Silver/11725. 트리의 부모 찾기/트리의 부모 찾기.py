from queue import Queue
import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())
nodes=[[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b= map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

root=[0]*(N+1)

def dfs(nodes,now, visited):
    visited[now]=True
    for next in nodes[now]: #새로 받은 now의 요소들을 반복
        if not visited[next]: #next가 방문리스트에 없으면
            root[next]=now
            dfs(nodes, next, visited)

visited=[False]*(N+1)
dfs(nodes,1,visited)

for q in range(2,N+1):
    print(root[q])          