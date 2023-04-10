import sys
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
cnt=0

for i in range(n): #원소개수만큼 반복
    for j in range(2, l[i]+1): #소수찾기, 0과 1은 필요없어서 l[2]부터 시작, 원소값보다 1큰 수까지
        if l[i]==j:#원소값이 증가값이랑 같으면
            cnt+=1
        if l[i]%j==0:
            break
print(cnt)