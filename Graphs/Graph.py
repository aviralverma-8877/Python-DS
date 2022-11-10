from queue import Queue

input = [
    [0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,1,0,0,1,0,0],
    [0,1,0,0,1,0,0],
    [0,0,1,1,0,1,1],
    [0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0],
]

class Graphs:
    def __init__(self, input, start, ele_count) -> None:
        self.adj_matrix = input
        self.q = Queue()
        self.start = start
        self.ele_count = ele_count
        self.visited = [0 for i in range(ele_count)]

    def bfs(self):
        print(self.start, end="")
        self.visited[self.start] = 1
        self.q.put(self.start)

        while( not self.q.empty()):
            i = self.q.get()
            for j in range(1, self.ele_count):
                if(self.adj_matrix[i][j] == 1 and self.visited[j] == 0):
                    print(j, end="")
                    self.visited[j] = 1
                    self.q.put(j)

    def dfs(self, i = None):
        if i == None:
            i = self.start
        if(self.visited[i] == 0):
            print(i, end="")
            self.visited[i] = 1
            for j in range(1, self.ele_count):
                if(self.adj_matrix[i][j] == 1 and self.visited[j] == 0):
                    self.dfs(j)

# bfsg = Graphs(input, 4, 7)
# bfsg.bfs()

dfsg = Graphs(input, 4, 7)
dfsg.dfs()
