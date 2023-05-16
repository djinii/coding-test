import sys
input=sys.stdin.readline
students=[]
students_list=[]
for _ in range(1,29):
    students.append(int(input().strip()))
for i in range(1,31):
    if(i not in students):
        print(i)