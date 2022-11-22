class Solution:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.mapper = {}
    
    def move(self, row, col):
        if row == 0 or col == 0:
            return 0
        if row == 1 and col == 1:
            return 1
        if str(row)+"-"+str(col) in self.mapper:
            return self.mapper[str(row)+"-"+str(col)]
        value = self.move(row-1,col)+self.move(row, col-1)
        self.mapper[str(row)+"-"+str(col)] = value
        return value

s = Solution(30,30)
print(s.move(30,30))