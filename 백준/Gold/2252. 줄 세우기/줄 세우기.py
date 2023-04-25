from queue import Queue
import sys
n,m=map(int,sys.stdin.readline().split())

connection = list([] for _ in range(n + 1)) #n이 3일때 [[],[],[],[]]
P_num=list(0 for _ in range(n+1)) #부모개수 리스트 [0,0,0,0]
answer=[]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    connection[a].append(b) #([],[3],[3],[])
    P_num[b]+=1 #(0,0,0,2)
visited=Queue()
top=Queue()

for i in range(1,n+1): #부모노드가 없으면 큐에 넣어라
    if P_num[i]==0:
        visited.put(i)
#큐에 값이 있을 때, visited[0]의 값을 빼고 now에 넣어줌, 그 now값을 answer리스트에 넣어준다
while visited.qsize()>0:
    now=visited.get()
    answer.append(now)
    #connection에서 인덱스 번호 (visited[0])=now의 자식노드를 반복한다, next값의 부모개수를 하나씩 줄이고 부모개수가 0이되면 visited에 넣어준다 
    for next in connection[now]:
        P_num[next]-=1
        if P_num[next]==0:
            visited.put(next)
for res in answer:
    sys.stdout.write(f'{res} ')
