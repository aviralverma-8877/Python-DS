# https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/
input = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 0, 0, 0]
]


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        '''
            Sample:
            [
                [0 0 1 1 1 1 0]
                [0 0 0 1 1 1 1]
                [0 0 0 1 1 1 0]
                [0 1 0 0 0 0 0]
            ]
            Approach:
                1. Traverse the matrix untill we find 1.
                2. Using that element perform breath first search in left and bottom
                3. Once reached and 0 or boundry, return steps.
        '''
        y = 0
        x = 0
        max_size = 0
        for i in enumerate(A):
            row_index = i[0]
            row = i[1]
            for j in enumerate(row):
                col_index = j[0]
                ele = j[1]
                if ele == 1:
                    elements = self.perform_search(row_index, col_index, A)
                    if max_size < elements:
                        max_size = elements
                        y = row_index
                        x = col_index
        return [max_size, y, x]
        
    def perform_search(self, i, j, matrix):
        size_y = len(matrix)
        size_x = len(matrix[0])
        row = i
        col = j
        height = 0
        breath = None
        # Checking in down direction
        while(row < size_y and matrix[row][col] == 1):
            #checking in left direction
            row_breath = 0
            while(col < size_x):
                if matrix[row][col] == 1:
                    row_breath += 1
                else:
                    break
                col += 1
            if breath == None:
                breath = row_breath
            else:
                breath = min(breath, row_breath)
            height += 1
            row += 1
            col = j
        print(height,breath, i, j)
        return height*breath

s = Solution()
print(s.maximalRectangle(input))
