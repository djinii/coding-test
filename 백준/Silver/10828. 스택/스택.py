import sys
n=int(sys.stdin.readline())

stack=[]

for i in range(n):
    od = list(map(str,sys.stdin.readline().split()))
    if od[0]=='push':
        stack.append(od[1])
    elif od[0]=='top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print('-1')

    elif od[0]=='pop':
        if len(stack)!=0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print('-1')
    elif od[0]=='size':
        print(len(stack))

    elif od[0]=='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')
