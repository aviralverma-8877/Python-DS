class Queue:
    def __init__(self, size) -> None:
        self.front = -1
        self.rear = self.front
        self.size = size
        self.q = [None]*size
    
    def enqueue(self, data):
        if(self.rear == len(self.q)-1):
            print("queue is full")
            return

        self.rear += 1
        self.q[self.rear] = data

    def dequeue(self):
        if(self.front == self.rear):
            print("Queue is empty")
            return

        self.front += 1
        x = self.q[self.front]
        self.q[self.front] = None
        if(self.front == self.rear):
           self.front = self.rear = -1
        return x
    
    def display(self):
        if(self.front == self.rear):
            print("Queue is empty")
            return
        
        for i in range(self.front+1, self.rear+1):
            print(self.q[i])

q = Queue(10)
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

q.display()

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