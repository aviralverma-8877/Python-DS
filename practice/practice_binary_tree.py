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
        self.root = None
        self.pre_order = []
        self.in_order = []
        self.post_order = []
    
    def create(self):
        queue = []
        if self.root == None:
            data = input("Enter the root node data: ")
            node = TreeNode()
            node.set_data(data)
            self.root = node
        queue.append(self.root)
        while(len(queue)!=0):
            node = queue.pop(0)
            left_data = input(f"Enter the left node data of {node.get_data()}: ")
            if left_data != '-1':
                t = TreeNode()
                t.set_data(left_data)
                node.set_left(t)
                queue.append(node.get_left())

            right_data = input(f"Enter the right node data of {node.get_data()}: ")
            if right_data != '-1':
                t = TreeNode()
                t.set_data(right_data)
                node.set_right(t)
                queue.append(node.get_right())
        return self.root

    # def pre_order_traversal(self, node):
    #     if node == None:            
    #         return
    #     else:
    #         self.pre_order.append(node.get_data())
    #         self.pre_order_traversal(node.get_left())
    #         self.pre_order_traversal(node.get_right())

    # def in_order_traversal(self, node):
    #     if node == None:            
    #         return
    #     else:
    #         self.in_order_traversal(node.get_left())
    #         self.in_order.append(node.get_data())
    #         self.in_order_traversal(node.get_right())

    # def post_order_traversal(self, node):
    #     if node == None:            
    #         return
    #     else:
    #         self.post_order_traversal(node.get_left())
    #         self.post_order_traversal(node.get_right())
    #         self.post_order.append(node.get_data())

    def pre_order_traversal(self):
        stack = []
        node = self.root
        while(len(stack)>0 or node!=None):
            if node == None:
                node = stack.pop()
                node = node.get_right()
            else:
                stack.append(node)
                self.pre_order.append(node.get_data())
                node = node.get_left()

    def in_order_traversal(self):
        stack = []
        node = self.root
        while(len(stack)>0 or node!=None):
            if node == None:
                node = stack.pop()
                self.in_order.append(node.get_data())
                node = node.get_right()
            else:
                stack.append(node)
                node = node.get_left()
    
    def post_order_traversal(self):
        stack = []
        node = self.root
        while(len(stack)>0 or node!=None):
            if node == None:
                node = stack.pop()
                node = node.get_right()
            else:
                stack.append(node)
                node = node.get_left()


s = Tree()
s.create()
s.pre_order_traversal()
s.in_order_traversal()
s.post_order_traversal()
print(s.pre_order)
print(s.in_order)
print(s.post_order)