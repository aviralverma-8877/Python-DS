input = [
    [1 , 0 , 0 , 0 , 0 , 0, 1],
    [0 , 1 , 0 , 1 , 1 , 1, 1],
    [0 , 0 , 1 , 0 , 1 , 0, 0],
    [1 , 1 , 0 , 0 , 1 , 0, 0],
    [1 , 0 , 1 , 1 , 0 , 0, 1],
    [1 , 0 , 0 , 0 , 0 , 1, 0]
]

class Solution:
    def __init__(self, inp) -> None:
        self.orignal = inp

    def rotate_matrix(self, m, x, y):
        rotated_matrix = [[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(0, x):
            for j in range(0, y):
                rotated_matrix[j][i] = m[i][j]
        return rotated_matrix

    def nones_to_zeros(self, m, x, y):
        for i in range(0, x):
            for j in range(0, y):
                if(m[i][j] == None):
                    m[i][j] = 0
        return m

    def superimpose_matrix(self, m, n, x, y):
        superimposed = [[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(0, len(m)):
            for j in range(0, len(m)):
                if(m[i][j] == n[i][j] == 1):
                    superimposed[i][j] = 1
        return superimposed

    def removeIslandonedir(self, n, x, y):
        m = [[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(0, x):
            connection = True
            for j in range(0, y):
                if(connection):
                    if(n[i][j] == 0):
                        connection = False
                    else:
                        m[i][j] = None
                else:
                    if(n[i][j] == None):
                        connection = True
                    if(n[i][j] == 1):
                        m[i][j] = n[i][j]
            connection = True
            for j in range(len(n[i])-1, -1, -1):
                if(connection):
                    if(n[i][j] == 0):
                        connection = False
                    else:
                        m[i][j] = None
                else:
                    if(n[i][j] == None):
                        connection = True
                    if(n[i][j] == 1):
                        if(m[i][j] != None):
                            m[i][j] = n[i][j]
        return m

    def removeIsland(self):
        removed_island_orginal = [[0 for i in range(len(self.orignal[0]))] for j in range(len(self.orignal))]
        removed_island_rotated = [[0 for i in range(len(self.orignal[0]))] for j in range(len(self.orignal))]
        
        removed_island_orginal = self.removeIslandonedir(self.orignal, len(self.orignal)-1, len(self.orignal[0])-1)
        removed_island_rotated = self.rotate_matrix(removed_island_orginal, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        removed_island_rotated = self.removeIslandonedir(removed_island_rotated, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)

        removed_island_orginal = self.nones_to_zeros(removed_island_orginal, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        removed_island_rotated = self.nones_to_zeros(removed_island_rotated, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        removed_island_rotated = self.rotate_matrix(removed_island_rotated, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        removed_island_rotated = self.rotate_matrix(removed_island_rotated, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        removed_island_rotated = self.rotate_matrix(removed_island_rotated, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        superimposed = self.superimpose_matrix(removed_island_orginal, removed_island_rotated, len(removed_island_rotated)-1, len(removed_island_rotated[0])-1)
        return superimposed


s = Solution(input)
result = s.removeIsland()
for i in range(0, len(result)):
    for j in range(0, len(result[i])):
        print(result[i][j], end=" ")
    print("")