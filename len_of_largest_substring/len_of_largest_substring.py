# s = "abcbiefgh"
# seen = {}
# start = l = 0
# for i, e in enumerate(s):
#     if e in seen and seen[e] >= start:
#         start = seen[e] + 1
#     seen[e] = i
#     l = max(l, i - start + 1)
# print(l)

def longestUniqueSubsttr(string):
    # last index of every character
    last_idx = {}
    max_len = 0

    # starting index of current
    # window to calculate max_len
    start_idx = 0

    for i in range(0, len(string)):

        # Find the last index of str[i]
        # Update start_idx (starting index of current window)
        # as maximum of current value of start_idx and last
        # index plus 1
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)

        # Update result if we get a larger window
        max_len = max(max_len, i - start_idx + 1)

        # Update last index of current char.
        last_idx[string[i]] = i

    return max_len

string = "geeksforgeeks"
length = longestUniqueSubsttr(string)
print(length)