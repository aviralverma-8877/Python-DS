inp_1 = ([1,2,3,9], 8)
inp_2 = ([1,2,4,4], 8)
inp_3 = ([1,2,5,8,10], 9)

class Solution:
    def __init__(self, inp):
        self.arr = inp[0]
        self.sum = inp[1]
        self.m = []
    
    def create_map(self):
        considered = []
        for i in self.arr:
            r = self.sum - i
            
            if(i not in considered):            #O()
                self.m.append((i,r))

            considered.append(i)
            considered.append(r)
        return False
    
    def start(self):
        pairs = []
        self.create_map()                       #O(n)
        for i in self.m:
            if i[0] in self.arr:                #O(n)
                if i[1] in self.arr:            #O(n)
                    pairs.append(i)
        return pairs
s = Solution(inp_2)
print(s.start())