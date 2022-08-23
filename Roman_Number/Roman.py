class Solution:
    def __init__(self):
        #self.i = 0
        self.cou = 0
        self.dict1 = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }

    def cal(self,fir,sec):
        return (self.dict1[sec] - self.dict1[fir])
    def romanToInt(self, s: str) -> int:
        i = 0
        self.dict1 = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }
        while i<len(s):
            if s[i] in self.dict1.keys():
                if (s[i] == "I") and (i+1 < len(s)) and (s[i+1] == "V" or s[i+1] == "X") :
                    self.cou += self.cal(s[i],s[i+1])
                    i = i+1
                elif (s[i] == "X") and (i+1 < len(s)) and (s[i+1] == "L" or s[i+1] == "C") :
                    self.cou += self.cal(s[i],s[i+1])
                    i = i+1
                elif (s[i] == "C") and (i+1 < len(s)) and (s[i+1] == "D" or s[i+1] == "M") :
                    self.cou += self.cal(s[i],s[i+1])
                    i = i+1
                else:
                    self.cou += self.dict1[s[i]]
            else:
                print("Invalid Key")
            i += 1

        return self.cou

x = Solution()
print(x.romanToInt("MCMXCIV"))