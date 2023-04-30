import sys
n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
answer=[1]*n
for i in range(1,n):
    for j in range(i+1):
        if numbers[i]>numbers[j]:
            answer[i]=max(answer[j]+1,answer[i])
print(max(answer))