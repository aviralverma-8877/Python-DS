#https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int):
        ele = "()"
        l = ["()"]
        for i in range(0, n-1):
            o = []
            for m in l:
                for j in range(0, len(m)+1):
                    k = list(m)
                    k.insert(j,ele)
                    p = ''.join(k)
                    if p not in o:
                        o.append(p)
            l = o
        return l

s = Solution()
s.generateParenthesis(3)