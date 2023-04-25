import sys
from collections import deque

input = sys.stdin.readline

def dfs(edges, v, visited): #n_list, v, visited
    visited[v] = True
    print(v, end=' ') #v값을 출력(3)
    for e in edges[v]: #새로 받은 v의 요소들을 반복
        if not visited[e]: #e가 방문리스트에 없으면
            dfs(edges, e, visited) #재귀

def bfs(edges, v, visited):
    queue = deque([v]) #v의값을 큐에 넣는거 (v가 3일때 3을 큐에 넣기)
    visited[v] = True #방문한걸로 바꾸기

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for e in edges[now]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True


n, m, v = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, n + 1):
    edges[i].sort()

visited = [False] * (n + 1)
dfs(edges, v, visited)
print()

visited = [False] * (n + 1)
bfs(edges, v, visited)
print()