class Solution:
    def generate(self, numRows):
        '''
            [1] -> [1,1] -> [1,2,1] -> [1,3,3,1]
        '''
        l = [[1]]
        if numRows == 1:
            return l
        for i in range(numRows-1):
            last_array = l[-1].copy()
            last_array.insert(0,0)
            last_array.append(0)
            new_array = []
            for i in range(0, len(last_array)-1):
                j = last_array[i] + last_array[i+1]
                new_array.append(j)
            l.append(new_array)
        return l
s = Solution()
for i  in (s.generate(25)):
    print(i)