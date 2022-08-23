x = "Charlie David Anna"
name_stu = list(x.split(" "))
print(name_stu)
name_final = []
for names in name_stu:
    x = open("People.txt", "r")
    m = [line.strip() for line in x.readlines()]
    if names in m:
        name_final.append(names)
    x.close()
print(name_final)
y = open("Nearby_Friends.txt", "w")
for insert_names in name_final:
    y.write(insert_names)
    y.write("\n")
y.close()

z = open("Nearby_Friends.txt", "r")
print(z.readlines())
