"""
replace 5 1's with single 1 

"""
x = "011111100001111001111"
y = ""
count = 0
for i in range(len(x)):
    if x[i] == "1":
        count += 1
    else:
        if count < 5 and count != 0:
            y += "1"*count
        y += "0"
        count = 0
    
    if count == 5:
        y += "1"
        count = 0
if count < 5 and count != 0:
    y += "1"*count

print(y)

