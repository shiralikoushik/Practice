def isbalanced(seq):
    while True:
        if "()" in seq:
            seq = seq.replace("()", "")
        elif "{}" in seq:
            seq = seq.replace("{}", "")
        elif "[]" in seq:
            seq = seq.replace("[]", "")
        else:
            return not seq


s = "[({{[}}){}[]]"
print("Given string is balanced:", isbalanced(s))
