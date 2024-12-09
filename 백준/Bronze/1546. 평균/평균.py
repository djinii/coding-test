n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

new_scores = [(score / max_score) * 100 for score in scores]

avg = sum(new_scores) / n

print(avg)