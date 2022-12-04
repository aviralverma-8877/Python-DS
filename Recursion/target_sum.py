class Solution:
    def __init__(self) -> None:
        self.mapper = {}
        self.l = []
    def can_sum(self, target, numbers):
        if target == 0:
            return True
        if target < 0:
            return False
        
        for i in numbers:
            if (target-i) in  self.mapper:
                return self.mapper[target-i]
            n = numbers.copy()
            n.remove(i)
            value = self.can_sum(target-i, n)
            self.mapper[target-i] = value
            if value == True:
                self.l.append(i)
                return True
        return False

s = Solution()
print(s.can_sum(11,[2,3,4,6,5]))
print(s.l)