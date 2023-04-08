t=int(input())
for i in range(t):
    s=0
    avg=0
    count=0
    high=0
    std=list(map(int,input().split()))
    for b in range(1,len(std)):
        s=s+std[b]
    avg=s/std[0]
    for x in range(1,len(std)):
        if(std[x]>avg):
            count+=1
    high=(count/std[0])*100
    print(f"{high:.3f}%")