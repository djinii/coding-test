numbers = {'ABC':3, 'DEF':4,'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8,'TUV':9, 'WXYZ':10}
word = input()
result = 0
for w in word :
    for key in numbers :
        if w in key :
            result += numbers[key]

print(result)