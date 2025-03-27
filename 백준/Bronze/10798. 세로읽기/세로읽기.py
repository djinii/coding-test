ans = [""]*15
for i in range(5) :
    s = input()
    for j in range(len(s)) :
        ans[j] += s[j]
print(*ans, sep="")