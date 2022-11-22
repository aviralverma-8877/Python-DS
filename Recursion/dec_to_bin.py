class Solution:
    def __init__(self, input) -> None:
        self.input = input
    
    def dec_to_bin(self, d):
        if d <= 1:
            return str(d)
        else:
            return self.dec_to_bin(int(d/2))+str(int(d%2))

s = Solution(233)
print(s.dec_to_bin(s.input))