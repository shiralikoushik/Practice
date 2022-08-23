ques = open("Q_and_A.txt", "r")
question = [line.strip() for line in ques.readlines()]
ques.close()
user_ans = 0
actual_ans = 0
for q in question:
    que, res = q.split("=")
    user_res = input(f"what is the answer of {que} = ")
    if user_res == res:
        user_ans += 1
        actual_ans += 1
    else:
        actual_ans += 1

print(user_ans, actual_ans)

op_file = open("Result.txt", "w")
op_file.write(f"Your Final Score is {user_ans}/{actual_ans}")
op_file.close()
