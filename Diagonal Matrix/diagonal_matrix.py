class DiagMatrix:
    def __init__(self,size):
        self.size = size
        self.matrix = [0]*size
    
    def add_element(self, ele, m, n):
        if(m==n):
            if(m<self.size):
                self.matrix[m] = ele

    def display(self):
        for i in range(0,self.size):
            for j in range(0, self.size):
                if(i==j):
                    print(self.matrix[i], end="")
                else:
                    print(0, end="")
            print("")


diag_matrix = DiagMatrix(5)
diag_matrix.add_element(1,0,0)
diag_matrix.add_element(2,1,1)
diag_matrix.add_element(3,2,2)
diag_matrix.add_element(4,3,3)
diag_matrix.add_element(5,4,4)
diag_matrix.add_element(6,5,5)

diag_matrix.display()