remainders = []

for i in range(10) :
    n = int(input())
    remainders.append(int(n%42))
    
print(len(set(remainders)))