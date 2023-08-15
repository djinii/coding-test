import sys
input = sys.stdin.readline
n, m = map(int,input().split())
cards = list(map(int,input().split()))[:n]
cards.sort(reverse=True)
sum_list = [0]
for i in range(n):
    if(sum == m):
        break
    else:
        for j in range(i+1, n):
            if(sum == m):
                break
            elif(cards[i] + cards[j]>m):
                j += 1
            else:
                for q in range(j+1, n):
                    sum = cards[i] + cards[j] + cards[q]
                    if(m < sum):
                        q+=1
                    else:
                        if(sum>=max(sum_list)):
                            sum_list.append(sum)
                        if(m == sum):
                            break
print(max(sum_list))