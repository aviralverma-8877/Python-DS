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
    
    def set_node(self, node):
        self = node

class CreateTree:
    def __init__(self) -> None:
        self.q = Queue()
        self.root_node = None
    
    def start(self):
        root = input("What is the root value:")
        self.root_node = TreeNode()
        self.root_node.set_data(int(root))
        self.q.enqueue(self.root_node)
        while(not self.q.empty()):
            node = self.q.dequeue()
            left = input(f"Enter the value for left child of {node.get_data()}:")
            if(left != "-1"):
                t = TreeNode()
                t.set_data(int(left))
                node.set_left(t)
                self.q.enqueue(t)
            right = input(f"Enter the value for right child of {node.get_data()}:")
            if(right != "-1"):
                t = TreeNode()
                t.set_data(int(right))
                node.set_right(t)
                self.q.enqueue(t)
        return

    def serialize_in_order(self, node, ser = []):
        if node != None:
            self.serialize_in_order(node.get_left(), ser)
            ser.append(node.get_data())
            self.serialize_in_order(node.get_right(), ser)
    
    def serialize_pre_order(self, node, ser = []):
        if node != None:
            ser.append(node.get_data())
            self.serialize_pre_order(node.get_left(), ser)
            self.serialize_pre_order(node.get_right(), ser)

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

    def deserialize(self, pre_order, in_order):
        m = self.gen_mapper(in_order)
        if self.root_node == None:
            self.root_node = TreeNode()
            self.root_node.set_data(pre_order[0])
        l = pre_order[1:]
        while len(l) > 0:
            node = self.root_node
            p = l[0]
            l = l[1:]
            method = None
            while node != None:
                if(m[p-1]<m[node.get_data()-1]):
                    method = node.set_left
                    node = node.get_left()                    
                else:
                    method = node.set_right
                    node = node.get_right()
            n = TreeNode()
            n.set_data(p)
            method(n)
        return self.root_node

        
    
    def gen_mapper(self, l):
        mapper = [None for i in range(max(l))]
        for i in enumerate(l):
            index = i[0]
            ele = i[1]
            mapper[ele-1] = index
        return mapper


class BinaryTree:
    def __init__(self) -> None:
        self.root_node = None

    def insert(self, node, key):
        t = None
        if node == None:
            t = TreeNode()
            t.set_data(key)           
            return t

        if key < node.get_data():
            node.set_left(self.insert(node.get_left(), key))
        elif key > node.get_data():
            node.set_right(self.insert(node.get_right(), key))
        return node

    def create(self, arr):
        for i in arr:
            self.root_node = self.insert(self.root_node, i)

    def binary_search(self, key, node):
        if node == None:
            return False
        if key == node.get_data():
            return True
        elif key < node.get_data():
            return self.binary_search(key, node.get_left())
        elif key > node.get_data():
            return self.binary_search(key, node.get_right())

ct = CreateTree()
ct.start()

ser_in_order = []
ct.serialize_in_order(ct.root_node,ser_in_order)
print(ser_in_order)

ser_pre_order = []
ct.serialize_pre_order(ct.root_node,ser_pre_order)
print(ser_pre_order)

dst = CreateTree()
dst.deserialize(ser_pre_order, ser_in_order)
pass
# ct.traverse_pre_order(ct.root_node)
# print()
# ct.traverse_in_order(ct.root_node)
# print()
# ct.traverse_post_order(ct.root_node)
# print()
# ct.for_traverse_pre_order()
# print()
# ct.for_traverse_in_order()
# print()
# ct.traverse_level_order()
# print()
# key = input("Key to search:")
# print(ct.binary_search(key, ct.root_node))

# bst = BinaryTree()
# bst.create(ser)
# pass
# print(bst.binary_search(84, bst.root_node))