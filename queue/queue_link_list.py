import gc

class Node:
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
        node = Node()
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
    
q = Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(4)
q.enqueue(10)
q.enqueue(11)
q.enqueue(15)
q.enqueue(25)
q.enqueue(30)


q.display()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

q.display()

q.enqueue(1)
q.enqueue(5)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(15)
q.enqueue(25)
q.enqueue(30)

q.display()