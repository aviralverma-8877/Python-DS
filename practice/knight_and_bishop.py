#https://www.youtube.com/watch?v=L8tY9gSfHz4

class Solution:
    def __init__(self, size, knight_pos, bishop_pos, knight_dest):
        self.knight_pos = knight_pos
        self.bishop_pos = bishop_pos
        self.knight_dest = knight_dest
        self.size = size
    
        self.bishops_alive = True
        self.bishop_range = [[0 for i in range(self.size)] for j in range(self.size)]
        self.fill_bishops_range()
        self.knight_moves = [
                [2  ,  1],
                [2  , -1],
                [-2 ,  1],
                [-2 , -1],
                [1  ,  2],
                [-1 ,  2],
                [1  , -2],
                [-1 , -2]
            ]

    def move_kight(self, knight_pos, bishops_alive, past_moves = []):
        if knight_pos in past_moves:
            return None
        past_moves.append(knight_pos)
        kx = knight_pos[0]
        ky = knight_pos[1]
        value = None
        for step in self.knight_moves:
            new_knight_pos = [kx+step[0],ky+step[1]]
            if self.check_knights_move(new_knight_pos, bishops_alive):
                knight_pos = new_knight_pos
                print(knight_pos)
                if knight_pos == self.knight_dest:
                    return []
                if bishops_alive:
                    bishops_alive = self.knight_killing_bishop(knight_pos)
                value = self.move_kight(knight_pos, bishops_alive, past_moves)
                if value != None:
                    value.append([knight_pos])
                else:
                    print("---------------------")
        return value

    def check_knights_move(self, knight_pos, bishops_alive):
        x = knight_pos[0]
        y = knight_pos[1]
        #Limit knights move in the board
        if x >= self.size:
            return False
        if y >= self.size:
            return False
        if x < 0:
            return False
        if y < 0:
            return False
        
        #Knight is not in bishops range
        if bishops_alive:
            if self.bishop_range[x][y] == 1:
                return False

        return True

    def knight_killing_bishop(self, knight_pos):
        x = knight_pos[0]
        y = knight_pos[1]
        if [x,y] == self.bishop_pos:
            return False
        return True

    def fill_bishops_range(self):
        #UP-LEFT
        i = self.bishop_pos[0]
        j = self.bishop_pos[1]
        while(i>=0 and j>=0):
            self.bishop_range[i][j] = 1
            i -= 1
            j -= 1
        #UP-RIGHT
        i = self.bishop_pos[0]
        j = self.bishop_pos[1]
        while(i<self.size and j>=0):
            self.bishop_range[i][j] = 1
            i += 1
            j -= 1
        #DOWN-RIGHT
        i = self.bishop_pos[0]
        j = self.bishop_pos[1]
        while(i<self.size and j<self.size):
            self.bishop_range[i][j] = 1
            i += 1
            j += 1
        #DOWN-LEFT
        i = self.bishop_pos[0]
        j = self.bishop_pos[1]
        while(i>=0 and j<self.size):
            self.bishop_range[i][j] = 1
            i -= 1
            j += 1
        i = self.bishop_pos[0]
        j = self.bishop_pos[1]
        self.bishop_range[i][j] = 0

s = Solution(8, [2,0], [3,4], [7,4])
print(s.move_kight(s.knight_pos, s.bishops_alive, []))