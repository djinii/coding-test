from collections import deque
import sys
N,M,K,X=map(int,sys.stdin.readline().split())
edges=[[]for _ in range(N+1)]

for i in range(M):
    A,B=map(int,sys.stdin.readline().split())
    edges[A].append(B)
visited=[False]*(N+1)
answer=[1]*(N+1)

queue=deque()
queue.append(X)

while queue:
    now=queue.popleft() #현재 방문하고 있는 도시
    for e in edges[now]: #그 도시에 인접해있는 다른 도시들
        if not visited[e]: #다른 도시들 중 방문을 안한도시면
            visited[e]=True #방문처리하고
            queue.append(e) #큐에 넣는다
            answer[e]+=answer[now]

for a in range(1, len(answer)):
    if a==X:continue
    if answer[a]-1==K:
        print(a) #index번호가 도시번호

answer=answer[a:X]+answer[X+1:] #시작도시전+시작도시이후=시작도시빼고 다
if not K+1 in answer:
    print(-1)