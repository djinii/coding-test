import sys
input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]

max_n = max(nums)

prime_numbers = [True] * (max_n + 1)
prime_numbers[0] = False
prime_numbers[1] = False

for i in range(2, int(max_n**0.5) + 1):
    if prime_numbers[i]:
        for j in range(i * i, max_n + 1, i):
            prime_numbers[j] = False

for n in nums:
    count = 0
    for p in range(2, n // 2 + 1):
        if prime_numbers[p] and prime_numbers[n - p]:
            count += 1
    print(count)
