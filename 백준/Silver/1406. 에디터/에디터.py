from sys import stdin

texts = stdin.readline().strip()
times = int(stdin.readline())

left_text = list(texts)  # 커서 왼쪽에 있는 문자들을 저장하는 리스트
right_text = []  # 커서 오른쪽에 있는 문자들을 저장하는 리스트

for _ in range(times):
    command = stdin.readline().strip()

    if command[0] == 'P':
        left_text.append(command[2])

    elif command[0] == 'L':
        if left_text:
            right_text.append(left_text.pop())

    elif command[0] == 'D':
        if right_text:
            left_text.append(right_text.pop())

    elif command[0] == 'B':
        if left_text:
            left_text.pop()

# 문자열을 합치는 과정에서 문자열 연산 대신 join() 메서드를 사용합니다.
result = ''.join(left_text + right_text[::-1])
print(result)
