def solution(friends, gifts):
    answer = 0

    gift_level = {name:0 for name in friends}
    gift_count = {friend:{name:0 for name in friends}for friend in friends}

    for gift in gifts :
        sender, receiver = gift.split()
        gift_count[sender][receiver] += 1
        gift_level[sender] += 1
        gift_level[receiver] -= 1

    next_gift = {friend:0 for friend in friends}

    for i in range(len(friends)) :
        for j in range(len(friends)) :
            if i == j :
                continue
            x = friends[i]
            y = friends[j]

            xToy_cnt = gift_count[x][y]
            yTox_cnt = gift_count[y][x]

            if xToy_cnt > yTox_cnt :
                next_gift[x] += 1
            elif xToy_cnt == yTox_cnt :
                if gift_level[x] > gift_level[y] :
                    next_gift[x] += 1

    answer = max(next_gift.values())
        
    return answer