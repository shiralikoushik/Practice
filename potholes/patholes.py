"""
Road n segments 
pathole - 'x' good segments - '.'
at a  time road filling machine can patch 3 segments. find the minimum number of patches required 
to repair the patholes in the road

ex: 
    .x..x - 2 patches
    xxxx - 2 patches
    xx.xxx.. - 2 patches
    x.xxxxx.x.. - 3 patches 

"""


road = "x.xxxxx.x.."
x = 0
count = 0
for i in road:
    if x == 3:
        x = 0
        count += 1
    if i == "x" and x >= 0:
        x = x + 1
    elif x > 0:
        x += 1

if x > 0:
    print(count + 1)
else:
    print(count)
