class Solution:
    def __init__(self, input) -> None:
        self.input = input
    
    def is_palindrome(self, s):
        if len(s) <= 1:
            return True
        else:
            return (s[0]==s[-1] and self.is_palindrome(s[1:-1]))

s = Solution("NISSIN")
print(s.is_palindrome(s.input))