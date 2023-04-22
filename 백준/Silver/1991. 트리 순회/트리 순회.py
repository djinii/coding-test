import sys
n=int(sys.stdin.readline())
d={}
for i in range(n):
    m, l, r=sys.stdin.readline().split()
    d[m]=[l, r]
    
def pre(m):    
    if m == '.':
        return 
    print(m,end="")
    pre(d[m][0]) 
    pre(d[m][1]) 

def inorder(m):
    if m=='.':
        return
    inorder(d[m][0]) 
    print(m,end="")
    inorder(d[m][1]) 

def post(m):
    if m=='.':
        return
    post(d[m][0]) 
    post(d[m][1]) 
    print(m,end="")

pre('A')
print()
inorder('A')
print()
post('A')
print()
