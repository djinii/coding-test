import sys
input = sys.stdin.readline

a, b = map(int, input().split())

#한줄에 띄움구분해서 int형으로 입력받아 리스트에 저장
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

#a_li 요소를 b_li에 추가
for a_mem in a_li:
    b_li.append(a_mem)    

#오름차순으로 정렬
li = sorted(b_li)

#리스트의 요소들만 출력
output = ' '.join(map(str, li))
print(output)