n=int(input())
for i in range(n):
    score=0
    s=list(map(str, input().split('X')))
    for a in range(len(s)):
        l=len(s[a])
        score=score+(l*(l+1)//2)
    print(score)
  