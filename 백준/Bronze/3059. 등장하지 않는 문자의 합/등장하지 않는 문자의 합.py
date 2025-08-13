t = int(input())
for i in range(t) :
    sum = 0
    s = input()
    for char in set(s) :
        sum += ord(char)
    print(2015 - sum)