import sys
p=sys.stdin.readline().strip()
stack=[]
ppap=['P','P','A','P']
for i in p:
    stack.append(i)
    if stack[-4:] == ppap:
        for _ in range(3):
            stack.pop()
if stack == ppap or stack==['P']:
    print('PPAP')
else:
    print("NP")
