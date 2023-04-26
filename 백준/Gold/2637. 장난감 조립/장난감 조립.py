from queue import Queue
import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph=[[0]*(N+1)for _ in range(N+1)]
connection = [[]for _ in range(N+1)]
Ch_num=list(0 for _ in range(N+1)) 

for _ in range(M):
    X,Y,K=map(int,sys.stdin.readline().split())
    connection[Y].append((X,K))
    Ch_num[X]+=1
    
visited=Queue()

for i in range(1,N+1):
    if Ch_num[i]==0:
        visited.put(i) #자식없는 노드를 큐에 넣음
        graph[i][i]+=1

while visited.qsize()>0:
    Now=visited.get() #큐[0]을 가져오고 저장
    for next, K in connection[Now]: #now와 연결된 노드를 찾으면서 
        for e in range(1,N+1):#각 노드마다 값을 늘려준다.
            graph[next][e]+=graph[Now][e]*K
        Ch_num[next]-=1 #연결된 그 노드의 자식수를 지운다.
        if Ch_num[next]==0:
            visited.put(next)#자식이 없을 경우 visited에 넣는다.

for q in range(N+1):
    if graph[N][q]!=0:
        print(q, graph[N][q])
