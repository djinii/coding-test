import sys
input = sys.stdin.readline

string = input().strip()
finder = input().strip()

stack = []
finder_len = len(finder)

for char in string:
    stack.append(char)
    if len(stack) >= finder_len and ''.join(stack[-finder_len:]) == finder:
        del stack[-finder_len:]

result = ''.join(stack)

if result == "":
    print("FRULA")
else:
    print(result)
