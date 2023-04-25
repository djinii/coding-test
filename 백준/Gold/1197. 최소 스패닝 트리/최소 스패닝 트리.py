import sys
input = sys.stdin.readline

v, e = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(e)]
data.sort(key = lambda x : x[2]) #가중치를 기준으로 오름차순 정렬 
ans = 0 #간선의 합을 초기화
parent = [i for i in range(v+1)] #parent리스트 생성
def find(x): #x의 루트노드를 찾아 반환하는 함수
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b): #a,b 집합을 합치는 함수
    A = find(a)
    B = find(b)
    if A > B:
        parent[A] = B
    else:
        parent[B] = A

for a, b, c in data:
    if find(a) != find(b): #a와 b가 같은 집합이 아니면
        union(a, b) #합쳐라
        ans += c #간중치 합

print(ans)