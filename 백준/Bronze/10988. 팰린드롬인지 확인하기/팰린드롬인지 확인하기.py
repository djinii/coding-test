s = input()
flag = False
for i in range(len(s)) :
    if s[i] == s[-(1+i)] :
        flag = True
        pass
    elif i == len(s) // 2 :
        break
    else : 
        flag = False
        break
if flag : 
    print(1)
else :
    print(0)