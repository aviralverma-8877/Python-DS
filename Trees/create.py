import gc

class StackNode:
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
        node = StackNode(data)
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
    
    def empty(self):
        if self.top == None:
            return True
        return False



class QueueNode:
    def __init__(self) -> None:
        self.data = None
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
    
    def set_next(self, node):
        self.next = node


class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None

    def enqueue(self, data):
        node = QueueNode()
        node.set_data(data)
        if not node:
            print("Queue is full")
            return
        if(self.front ==  None):
            self.front = self.rear = node
            return

        self.rear.set_next(node)
        self.rear = node
        
    def dequeue(self):
        if(self.front == None):
            print("Queue is empty")
            return
        
        x = self.front.get_data()
        t = self.front
        self.front = self.front.get_next()
        del t
        gc.collect()
        return x

    def display(self):
        if(self.front == None):
            print("Queue is empty")
            return
        
        t = self.front
        while(t != None):
            print(t.get_data())
            t = t.get_next()
    
    def empty(self):
        if(self.front == None):
            return True
        return False    

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

class CreateTree:
    def __init__(self) -> None:
        self.q = Queue()
        self.root_node = None
    
    def start(self):
        root = input("What is the root value:")
        self.root_node = TreeNode()
        self.root_node.set_data(root)
        self.q.enqueue(self.root_node)
        while(not self.q.empty()):
            node = self.q.dequeue()
            left = input(f"Enter the value for left child of {node.get_data()}:")
            if(left != "-1"):
                t = TreeNode()
                t.set_data(left)
                node.set_left(t)
                self.q.enqueue(t)
            right = input(f"Enter the value for right child of {node.get_data()}:")
            if(right != "-1"):
                t = TreeNode()
                t.set_data(right)
                node.set_right(t)
                self.q.enqueue(t)
        return

    def traverse_pre_order(self, node):
        if node != None:
            print(node.get_data(), end="")
            self.traverse_pre_order(node.get_left())
            self.traverse_pre_order(node.get_right())
    
    def traverse_in_order(self, node):
        if node != None:
            self.traverse_in_order(node.get_left())
            print(node.get_data(), end="")
            self.traverse_in_order(node.get_right())

    def traverse_post_order(self, node):
        if node != None:
            self.traverse_post_order(node.get_left())
            self.traverse_post_order(node.get_right())
            print(node.get_data(), end="")
    
    def for_traverse_pre_order(self):
        node = self.root_node
        if(node == None):
            return
        s = Stack()
        while(not s.empty() or node != None):
            if(node != None):
                s.push(node)
                print(node.get_data(), end="")
                node = node.get_left()
            else:
                node = s.pop()
                node = node.get_right()

    def for_traverse_in_order(self):
        node = self.root_node
        if(node == None):
            return
        s = Stack()
        while(not s.empty() or node != None):
            if(node != None):
                s.push(node)
                node = node.get_left()
            else:
                node = s.pop()
                print(node.get_data(), end="")
                node = node.get_right()
    
    def traverse_level_order(self):
        node = self.root_node
        if(node == None):
            return
        q = Queue()
        q.enqueue(node)
        while(not q.empty() or node == None):
            node = q.dequeue()
            print(node.get_data(), end="")
            if(node.get_left() != None):
                q.enqueue(node.get_left())
            if(node.get_right() != None):
                q.enqueue(node.get_right())

ct = CreateTree()
ct.start()
ct.traverse_pre_order(ct.root_node)
print()
ct.traverse_in_order(ct.root_node)
print()
ct.traverse_post_order(ct.root_node)
print()
ct.for_traverse_pre_order()
print()
ct.for_traverse_in_order()
print()
ct.traverse_level_order()