import sys
import random
li=[]
ran=[0]*7
for _ in range(9):
    li.append(int(sys.stdin.readline()))
while True:
    ran[0],ran[1],ran[2],ran[3],ran[4],ran[5],ran[6]=random.sample(li,7)
    s=sum(ran)
    if s==100:
        ran.sort()
        break
for j in range(7):
    print(ran[j])