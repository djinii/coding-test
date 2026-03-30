def solution(board, moves):
    answer = 0
    stack = []
    for move in moves :
        for i in range(len(board)) :
            target = board[i][move-1]
            if target != 0 :
                board[i][move-1] = 0

                if len(stack) != 0 and stack[-1] == target :
                    stack.pop()
                    answer += 2
                else :
                    stack.append(target)
                break
    return answer