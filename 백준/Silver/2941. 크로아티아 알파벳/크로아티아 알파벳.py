c_alphabet = ['c=','c-', 'dz=', 'd-','lj', 'nj', 's=', 'z=']

word = input()
i = 0
count = 0
while i < len(word) :
    count += 1
    if word[i] == "d" :
        if word[i:i+3] == c_alphabet[2] :
            i += 3
            continue
    if word[i:i+2] in c_alphabet :
        i += 2
    else :
        i += 1

print(count)
        
    