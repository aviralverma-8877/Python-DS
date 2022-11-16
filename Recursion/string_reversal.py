class Solution:
    def __init__(self, input) -> None:
        self.input = input
    
    def reverse_string(self, s):
        if len(s) != 0:
            return self.reverse_string(s[1:])+s[0]
        return ""

s = Solution("hello world")
print(s.reverse_string(s.input))