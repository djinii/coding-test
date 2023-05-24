import sys
n=int(sys.stdin.readline())
my_cards = list(map(int,sys.stdin.readline().split()))[:n]
my_cards=set(my_cards)
m=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))[:m]

for i in range(m):
    if(cards[i] in my_cards) :
        print('1', end=" ")
    else :     
        print('0', end=" ")
print()