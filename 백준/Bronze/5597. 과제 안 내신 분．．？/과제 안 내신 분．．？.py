students = [0] * 30
[0, 1, 0, 1, 1, ]

for i in range(28) :
    n = int(input())
    students[n-1] = 1

a = students.index(0)
print(a+1)
students[a] = 1

a = students.index(0)
print(a+1)