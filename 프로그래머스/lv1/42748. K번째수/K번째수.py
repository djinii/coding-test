def solution(array, commands):
    answer = []
    new_arr=[]

    for j in range(len(commands)):
        a = commands[j][0]
        b = commands[j][1]
        c = commands[j][2]

        new_arr = array[a-1:(b)]
        new_arr.sort()

        answer.append(new_arr[c-1])
    return answer