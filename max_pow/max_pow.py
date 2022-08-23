def solution(N):

    i = 0
    max_pow = [0]
    while (2**i <= N):
        if (N % (2**i)) == 0:
            max_pow.append(i) 
        i += 1
    return max(max_pow)

print(solution(24))