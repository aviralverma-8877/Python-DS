#https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board, word):
        first_char = word[0]
        word = word[1:]
        for i in enumerate(board):
            row_index = i[0]
            row = i[1]
            for j in enumerate(row):
                col_index = j[0]
                ele = j[1]
                if ele == first_char:
                    if self.search(word, board, row_index, col_index):
                        return True
        return False
    def search(self, word, board, row, col):
        visited = []
        for char in word:
            print(char)
            queue = [[row,col]]
            while len(queue)>0:
                q = queue.pop(0)
                found = False
                r = row = q[0]
                c = col = q[1]
                visited.append([r,c])
                if row>0 and char == board[row-1][col] and [row-1,col] not in visited:
                    r = row-1
                    c = col
                    found = True
                if col>0 and char == board[row][col-1] and [row,col-1] not in visited:
                    c = col-1
                    r = row
                    found = True
                if row<(len(board)-1) and char == board[row+1][col] and [row+1,col] not in visited:
                    r = row+1
                    c = col
                    found = True
                if col<(len(board[0])-1) and char == board[row][col+1] and [row,col+1] not in visited:
                    c = col+1
                    r = row
                    found = True
                row = r
                col = c
                if found:
                    print(r,c)
                    queue.append([r,c])
        return True

s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")