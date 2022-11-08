class Matrix:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.matrix = [[0 for i in range(col)] for j in range(row)]
    
    def display(self):
        for row in range(0,self.row):
            for col in range(0, self.col):
                print(self.matrix[row][col], end="")
            print("")

    def add_element(self, ele, row, col):
        row -=1
        col -=1
        if(row <= self.row and col <= self.col):
            self.matrix[row][col] = ele

m = Matrix(5,5) 
m.add_element(5,2,4)
m.display()