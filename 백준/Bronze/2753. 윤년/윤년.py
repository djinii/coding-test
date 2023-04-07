y=int(input())

a=y%100
b=y%400
c=y%4

if b==0  or (c==0 and a!=0) :
    print("1")
else :
    print("0")