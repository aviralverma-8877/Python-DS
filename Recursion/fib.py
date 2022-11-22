class Solution:
    def __init__(self) -> None:
        self.mapper = {}
    def nth_in_fib(self, n):
        if n<2:
            return 1
        if n in self.mapper:
            return self.mapper[n]
        value = self.nth_in_fib(n-1) + self.nth_in_fib(n-2)
        self.mapper[n] = value
        return value
    
s = Solution()
print(s.nth_in_fib(55))