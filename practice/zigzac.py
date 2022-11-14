#https://leetcode.com/problems/zigzag-conversion/submissions/
# list of stack = [[P,A,Y],[*,P,*],......]

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = []
        S = list(s)
        count = 0
        while len(S) > 0:
            if(count%numRows == 0):
                stack = ["*" for i in range(numRows)]
                count = 1
            else:
                stack = [None for i in range(numRows)]
                ind = (count*-1)          #3 - (3%3) - 1 = 3-0-1 = 2
                stack[ind] = "*"
            for i in enumerate(stack):
                if(len(S) <= 0):
                    break
                index = i[0]
                ele = i[1]
                if ele == '*':
                    stack[index] = S[0]
                    S = S[1:]
            l.append(stack)
            count += 1
        print(l)
        s=""
        for i in range(0, numRows):
            for stack in l:
                if stack[i] != None and stack[i] != "*":
                    s += stack[i]
        return s