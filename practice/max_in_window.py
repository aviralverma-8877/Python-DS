#https://www.youtube.com/watch?v=OLuIHW4sXk4

class Solution:
    def __init__(self, l, k):
        self.l = l
        self.window = k
        self.mapper = [[] for i in range(len(l)-self.window+1)]
    
    def max_in_window(self):
        if self.window > len(self.l):
            return [max(self.l)]

        for i in range(0, len(self.l)-self.window+1):
            start = i
            end = i+self.window
            self.mapper[i] = self.l[start:end]
        result = []
        for i in self.mapper:
            result.append(max(i))
        return result

s = Solution([3,5,1,7,9,6,4], 8)
print(s.max_in_window())