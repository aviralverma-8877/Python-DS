#https://www.youtube.com/watch?v=QBX7RkhuyCA

Input = [
    [ 2 , 4,  5 ,  7 ],
    [ 3 , 8, 15 , 20 ],
    [ 6 , 9, 17 , 25 ]
]

class Solution:
    def __init__(self, inp) -> None:
        self.inp = inp
        self.max_x = len(inp[0])
        self.max_y = len(inp)
    
    def is_available(self, i):
        row = self.search_row(i)
        if row != False:
            ele = self.search_col(row, i)
            if ele != False:
                return True
            return False
        return False

    def search_col(self, row, i):
        l = 0
        h = len(self.inp)
        
        while (l<h):
            m = int((l+h)/2)
            if(i<row[m]):
                h = m-1
            elif(i > row[m]):
                l = m+1
            else:
                return row[m]
        return False

    def search_row(self, i):
        l = 0
        h = len(self.inp)
        
        while (l<=h):
            m = int((l+h)/2)
            if(i<self.inp[m][0]):
                h = m
            elif(i > self.inp[m][self.max_x-1]):
                l = m
            else:
                return self.inp[m]
        return False

s = Solution(Input)
print(s.is_available(15))