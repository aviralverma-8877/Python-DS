import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
        
    def set_next(self, node):
        self.next = node

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        node = Node(data)
        if not node:
            print("Stack overflow")
            return
        
        if self.top == None:
            self.top = node
            return
        
        node.set_next(self.top)
        self.top = node
    
    def pop(self):
        if self.top == None:
            print("Stack is Empty")
            return
        
        t = self.top
        self.top = self.top.get_next()
        x = t.data
        del t
        gc.collect()
        return x
    
    def display(self):
        if self.top == None:
            print("Stack is Empty")
            return

        t = self.top
        while(t != None):
            print(t.get_data())
            t = t.get_next()


stack = Stack()

stack.pop()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)

# 70
# 60
# 50
# 40
# 30
# 20
# 10

stack.pop()
stack.pop()

# 50
# 40
# 30
# 20
# 10

stack.display()