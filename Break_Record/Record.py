score = [10, 5, 20, 20, 4, 5, 2, 25, 1]
max_score = score[0]
min_score = score[0]
score_in = {"max": 0, "min": 0}
for i in range(1, len(score)):
    if score[i] > max_score:
        max_score = score[i]
        score_in["max"] += 1
    elif score[i] < min_score:
        min_score = score[i]
        score_in["min"] += 1

print(score_in["max"], score_in["min"])
