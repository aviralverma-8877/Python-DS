#https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        self.memo = {}
        return self.start_climbing(n, steps)
    
    def start_climbing(self, target, steps):
        if target in self.memo:
            return self.memo[target]
        if(target==0):
            return 1
        if(target < 0):
            return 0
        ways = 0
        for i in steps:
            ways += self.start_climbing(target-i, steps)
        self.memo[target] = ways
        return ways

class Solution1:                            #Without memonization
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        self.memo = []
        self.ways = 0
        self.start_climbing(n, steps)
        return self.ways
    
    def start_climbing(self, target, steps):
        if(target==0):
            self.ways += 1
            return True
        
        if(target>0):
            for i in steps:
                self.start_climbing(target-i,steps )

        return False

s = Solution()
print(s.climbStairs(4))
# 1 1 1 1
# 1 1 2 2
# 1 2 2 1
# 2 2 1 1
# 2 2