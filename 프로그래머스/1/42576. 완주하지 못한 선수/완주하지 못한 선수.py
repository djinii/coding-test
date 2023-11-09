def solution(participant, completion):
    answer = ''
    p_dict = {name:0 for name in participant}

    for name in participant:
        p_dict[name] += 1

    for name in completion:
        p_dict[name] -= 1

    for name, cnt in p_dict.items():
        if cnt > 0:
            answer = name
    return answer