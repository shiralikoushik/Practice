def generate(num):
    result = []
    for i in range(num):
        if i == 0:
            row = [1]
            result.append(row)
        else:
            j = 1
            row1 = [1]
            while j < i:
                row1.append(row[j-1] + row[j])
                j += 1
            row1.append(1)
            result.append(row1)
            row = row1
    return result
print(generate(5))