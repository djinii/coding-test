import sys
from collections import deque

def dfs(edges, v, visited):
    global cnt
    visited[v] = True
    for e in edges[v]:
        if not visited[e]:
            dfs(edges, e, visited) 

n=int(sys.stdin.readline())
e=int(sys.stdin.readline())
edges = [[]for _ in range((n+1))]
cnt=0
for _ in range(e):
    a, b=map(int,sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(n+1):
    edges[i].sort()

visited=[False]*(n+1)
dfs(edges,1,visited)

print(visited.count(True)-1)