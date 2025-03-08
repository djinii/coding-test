word = input()
result = [0] * 26

for i in word:
    result[ord(i.upper()) - 65] += 1

max_cnt = max(result)  
max_char = '?'
cnt = 0

for idx, count in enumerate(result):
    if count == max_cnt:
        if max_char == '?':  
            max_char = chr(idx + 65)
        else:  
            max_char = '?'
            break

print(max_char)
