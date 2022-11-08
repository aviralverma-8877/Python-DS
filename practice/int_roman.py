class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0
        s = self.handle_exp(s)
        print(s)
        for c in s:
            if c == "M":
                r += 1000
            if c == "D":
                r += 500
            if c == "C":
                r += 100
            if c == "L":
                r += 50
            if c == "X":
                r += 10
            if c == "V":
                r += 5
            if c == "I":
                r += 1
        return r
    
    def handle_exp(self, s: str) -> str:
        s = s.replace("IV","IIII")
        s = s.replace("IX","VIIII")
        s = s.replace("XL","XXXX")
        s = s.replace("XC","LXXXX")
        s = s.replace("CD","CCCC")
        s = s.replace("CM","DCCCC")
        return s
        

class Solution2:
    def intToRoman(self, num: int) -> str:
        th = int(num / 1000) * 1000
        th_rem = num % 1000
        
        hu = int(th_rem / 100) * 100
        hu_rem = th_rem%100
        
        te = int(hu_rem / 10) * 10
        te_rem = hu_rem % 10
        
        oc = te_rem
        ret = ""
# Once
        if self.handle_exp(oc):
            ret = self.handle_exp(oc) + ret
        else:
            for i in range (0, oc):
                ret = "I" + ret
            ret = ret.replace("IIIII","V")
# tense
        if self.handle_exp(te):
            ret = self.handle_exp(te) + ret
        else:
            for i in range(0, te, 10):
                ret = "X" + ret
            ret = ret.replace("XXXXX","L")
# hundreds
        if self.handle_exp(hu):
            ret = self.handle_exp(hu) + ret
        else:
            for i in range(0, hu, 100):
                ret = "C" + ret
            ret = ret.replace("CCCCC","D")
# thousand
        if self.handle_exp(th):
            ret = self.handle_exp(th) + ret
        else:
            for i in range(0, th, 1000):
                ret = "M" + ret
        return ret


    def handle_exp(self, d):
        if d == 4:
            return "IV"
        elif d == 9:
            return "IX"
        elif d == 40:
            return "XL"
        elif d == 90:
            return "XC"
        elif d == 400:
            return "CD"
        elif d == 900:
            return "CM"
        return False


sol = Solution2()
print(sol.intToRoman(1994))