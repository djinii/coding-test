def solution(num_list, n):
    answer = []
    answer += num_list[n:]
    answer += num_list[:n]

    return answer