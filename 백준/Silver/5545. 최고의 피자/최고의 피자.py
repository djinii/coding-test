n=int(input())
dough_price, topping_price = map(int,input().split())
dough_cal=int(input())
caloreies=[]

for _ in range(n):
    topping_cal=int(input())
    caloreies.append(topping_cal)

total_cal=dough_cal 
total_price=dough_price
caloreies.sort(reverse=True)

for i in range(n):
    if total_cal/total_price<(total_cal+caloreies[i])/(total_price+topping_price):
        total_cal+=caloreies[i]
        total_price+=topping_price
    else:
        break
print(int(total_cal/total_price))