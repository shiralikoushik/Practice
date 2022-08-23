import re

str1 = "BruceWayneIsBatman"

res = re.findall(r"[A-Z][a-z]+", str1)

print(" ".join(res).lower())
