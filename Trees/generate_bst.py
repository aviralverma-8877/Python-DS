input = [30,20, 10, 15, 25, 40, 50, 45]

class TreeNode:
    def __init__(self) -> None:
        self.data = None
        self.left = None
        self.right = None
    
    def get_data(self):
        return self.data

    def get_left(self):
        return self.left 

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

class Tree:
    def __init__(self) -> None:
        self.root_node = None
        self.stack = []
        self.pointer = None

    def list_to_bst(self, arr):
        if(self.root_node == None):
            self.root_node = TreeNode()
            self.root_node.set_data(arr[0])
            self.pointer = self.root_node 
        for i in arr[1:]:
            node = TreeNode()
            node.set_data(i)
            if(i<self.pointer.get_data()):
                self.stack.append(self.pointer)
                self.pointer.set_left(node)
                self.pointer = self.pointer.get_left()
            else:
                if(len(self.stack) == 0) or (i < self.stack[-1].get_data() and i > self.pointer.get_data()):
                    self.pointer.set_right(node)
                    self.pointer = self.pointer.get_right()
                else:
                    self.pointer = self.stack.pop()
                    self.pointer.set_right(node)
                    self.pointer = self.pointer.get_right()

t = Tree()
t.list_to_bst(input)
pass