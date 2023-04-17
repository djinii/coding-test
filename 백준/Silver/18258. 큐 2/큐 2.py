from collections import deque
import sys

t = int(sys.stdin.readline())
d = deque()

for i in range(t):
    input = list(map(str, sys.stdin.readline().split()))

    if input[0] == 'push':
        d.append(input[1])
    elif input[0] == "pop":
        if len(d) == 0:
            print('-1')
        else:
            print(d.popleft())
    elif input[0] == 'size':
        print(len(d))
    elif input[0] == "empty":
        if len(d) == 0:
            print('1')
        else:
            print('0')
    elif input[0] == 'front':
        if len(d) == 0:
            print('-1')
        else:
            print(d[0])
    elif input[0] == 'back':
        if len(d) == 0:
            print('-1')
        else:
            print(d[-1])
