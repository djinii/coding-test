def Euclidean(max, min) :
    while True :
        result = max % min
        if result == 0 :
            break
        max = min
        min = result
    return min
    
n = int(input())
trees = [int(input()) for _ in range(n)]
trees.sort()

# 간격
intervals = []
for j in range(n-1) :
    intervals.append(trees[j+1] - trees[j])

gcd_val = intervals[0]
for q in range(1, len(intervals)):
    gcd_val = Euclidean(gcd_val, intervals[q])

total_distance = trees[n-1] - trees[0]

result = total_distance // gcd_val + 1

print(result - n)
    
    
