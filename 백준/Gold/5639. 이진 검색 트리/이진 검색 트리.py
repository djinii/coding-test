import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(first, end):
    if first > end:
        return
    mid = end+1
    for i in range(first+1, end+1): #index 1~8까지
        if num_list[first] < num_list[i]: #50보다 클경우 걸림
            mid = i
            break
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(num_list[first])
    
postorder(0, len(num_list)-1)