class Queue:
    def __init__(self, size) -> None:
        self.front = 0    #Remember for circular queue, front and read should start from 0
        self.rear = self.front
        self.size = size
        self.q = [None]*(size)

    def enqueue(self, data):
        if(((self.rear+1) % self.size) == self.front):
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = data


    def dequeue(self):
        if(self.front == self.rear):
            print("Queue is Empty")
            return
        self.front = (self.front + 1) % self.size
        x = self.q[self.front]
        self.q[self.front] = None
        return x

    def display(self):
        if(self.front == self.rear):
            print("Queue is Empty")
            return
        
        index = self.front
        while(index != self.rear):
            index = (index + 1) % self.size
            print(self.q[index])



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