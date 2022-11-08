class Solution:
    def numberToWords(self, num: int) -> str:
        bi = int(num / 1000000000)
        bi_rem = num % 1000000000

        mi = int(bi_rem / 1000000)
        mi_rem = bi_rem % 1000000

        th = int(mi_rem / 1000)
        th_rem = mi_rem % 1000

        ret = ""
        if num == 0:
            ret = "Zero "
        if self.hun_text(th_rem) != "":
            ret = self.hun_text(th_rem) + ret
        if self.hun_text(th) != "":
            ret = self.hun_text(th) + "Thousand " + ret
        if self.hun_text(mi) != "":
            ret = self.hun_text(mi) + "Million " + ret
        if self.hun_text(bi) != "":
            ret = self.hun_text(bi) + "Billion " + ret

        return ret[:-1]

    def hun_text(self, d):
        hu = int(d / 100)
        hu_rem = d % 100
        oc = 0
        if hu_rem > 20:
            te = int(hu_rem / 10) * 10
            oc = hu_rem % 10
        else:
            te = hu_rem
        ret = ""

        if oc != 0 and self.num_text(oc) != "":
            ret = self.num_text(oc) + ret
        if self.num_text(te) != "":
            ret = self.num_text(te) + ret
        if self.num_text(hu) != "":
            ret = self.num_text(hu) + "Hundred " + ret

        return ret

    def num_text(self, d):
        if d == 1:
            return "One "
        if d == 2:
            return "Two "
        if d == 3:
            return "Three "
        if d == 4:
            return "Four "
        if d == 5:
            return "Five "
        if d == 6:
            return "Six "
        if d == 7:
            return "Seven "
        if d == 8:
            return "Eight "
        if d == 9:
            return "Nine "
        if d == 10:
            return "Ten "
        
        if d == 11:
            return "Eleven "
        if d == 12:
            return "Twelve "
        if d == 13:
            return "Thirteen "
        if d == 14:
            return "Fourteen "
        if d == 15:
            return "Fifteen "
        if d == 16:
            return "Sixteen "
        if d == 17:
            return "Seventeen "
        if d == 18:
            return "Eighteen "
        if d == 19:
            return "Nineteen "

        if d == 20:
            return "Twenty "
        if d == 30:
            return "Thirty "
        if d == 40:
            return "Forty "
        if d == 50:
            return "Fifty "
        if d == 60:
            return "Sixty "
        if d == 70:
            return "Seventy "
        if d == 80:
            return "Eighty "
        if d == 90:
            return "Ninety "
        else:
            return ""

sol = Solution()
print(sol.numberToWords(1000))