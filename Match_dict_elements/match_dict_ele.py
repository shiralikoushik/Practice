dic1 = {
        "pulto":"earth",
        "earth":"world",
        "world":"universe",
        "universe":"pulto"
}

s1 = "Sam on earth"
s2 = "Sam in pulto"
def eq(dic1,s1,s2):
    li1 = s1.split(" ")
    li2 = s2.split(" ")

    if len(li1) != len(li2):
        return False
    elif li1 == li2:
        return True
    else:
        for i in range(len(li1)):
            if li1[i] != li2[i]:
                if li1[i].lower() not in dic1.keys() and li2[i].lower() not in dic1.keys():
                    return False
                elif (dic1.get(li1[i].lower()) == li2[i].lower()) or (dic1.get(li2[i].lower()) == li1[i].lower()):
                    return True
                elif (li1[i].lower() not in dic1.keys() and li2[i].lower() not in dic1.values()) and (li2[i].lower() not in dic1.keys() and li1[i].lower() not in dic1.values()):
                    return False
                else:
                    if li1[i].lower() in dic1.keys() and li2[i].lower() in dic1.values():
                        x = li1[i].lower()
                        while x in dic1.keys():
                            if dic1[x].lower() == li2[i].lower():
                                return True
                            x = dic1[x].lower()
                        return False
                    else:
                        x = li2[i].lower()
                        while x in dic1.keys():
                            if dic1[x].lower() == li1[i].lower():
                                return True
                            x = dic1[x].lower()
                        return False                       


print(eq(dic1,s1,s2))

