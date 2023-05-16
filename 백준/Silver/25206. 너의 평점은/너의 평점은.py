import sys
input=sys.stdin.readline
credit = 0.0
summ = 0.0
average = 0.0
li = []
for i in range(20):
    input_str = input()
    input_list = input_str.split()
    li.append([float(input_list[-2]), input_list[-1]])

for j in range(20):
    if(li[j][-1]=='A+'):
        li[j][-1]=4.5
    elif(li[j][-1]=='A0'):
        li[j][-1]=4.0
    elif(li[j][-1]=='B+'):
        li[j][-1]=3.5
    elif(li[j][-1]=='B0'):
        li[j][-1]=3.0
    elif(li[j][-1]=='C+'):
        li[j][-1]=2.5
    elif(li[j][-1]=='C0'):
        li[j][-1]=2.0
    elif(li[j][-1]=='D+'):
        li[j][-1]=1.5
    elif(li[j][-1]=='D0'):
        li[j][-1]=1.0
    elif(li[j][-1]=='F'):
        li[j][-1]=0.0
    else:
        li[j][-1]=0.0
        li[j][-2]=0

    summ+=li[j][-2]*(li[j][-1])
    credit+=li[j][-2]
if(summ==0):
    average=0
else:
    average=summ/credit
    average = round(average, 6)
print("{:.6f}".format(average))
