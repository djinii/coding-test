import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))
n_list.sort()

def search(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for i in m_list:
    result=search(n_list,i,0,n-1)
    if result is not None:
        print(1)
    else:
        print(0)