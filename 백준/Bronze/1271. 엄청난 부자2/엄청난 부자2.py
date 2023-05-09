import sys
input=sys.stdin.readline
n, m = map(int, input().split())
quotient=n//m
remainder=n%m
print(quotient)
print(remainder)