"""
Challan for bike

Entry fee 2 rupees
First hour 3 rupees
From second hour 4 rupees per hour

Given Entery time and Exit time in HH:MM

if it is 2.5 hours -> 2(entry fee)+3(for first hour) +4*2 (2nd hour + 0.5 hours over 2)

Partial hours considered as next full hours

"""


def solution(E, L):
    # write your code in Python 3.6
    ET = list(map(int, E.split(":")))
    LT = list(map(int, L.split(":")))
    eh = ET[0]
    em = ET[1]
    lh = LT[0]
    lm = LT[1]
    ETotal = eh * 60 + em
    if lh > 24:
        Ltotal = (24 + lh) * 60 + lm
    else:
        Ltotal = lh * 60 + lm

    Time_diff = Ltotal - ETotal
    print(Time_diff)
    Time_spent_hours = Time_diff // 60
    print(Time_spent_hours)
    if Time_spent_hours > 1 and ((Time_diff % 60) == 0):
        return 2 + 3 + ((Time_spent_hours - 1) * 4)
    elif Time_spent_hours > 1 and ((Time_diff % 60) != 0):
        return 2 + 3 + ((Time_spent_hours) * 4)
    elif (Time_spent_hours == 1) and (Time_diff % 60 != 0):
        return 2 + 3 + 4
    else:
        return 2 + 3


print(solution("17:00", "18:48"))
