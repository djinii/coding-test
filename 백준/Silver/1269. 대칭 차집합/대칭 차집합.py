import sys
input = sys.stdin.readline

a, b=map(int, input().split())

a_li01 = set(map(int, input().split()))
b_li01 = set(map(int, input().split()))
cnt = 0

elements = a_li01.intersection(b_li01)
cnt = len(elements)

print((a - cnt)+(b - cnt))