class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.pre = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_pre(self):
        return self.pre

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node
    
    def set_pre(self, node):
        self.pre = node

class Stacked_list:
    def __init__(self) -> None:
        self.first = None
        self.last = self.first

    def prepend(self, node):
        if(self.first == self.last == None):
            self.last = self.first = node
            return
        node.set_next(self.first)
        self.first.set_pre(node)
        self.first = node
    
    def insert(self, n, index):
        t = self.first
        i = 0
        if(index == 0):
            self.prepend(n)
            return True
        elif(t == None):
            return False
        while(t != None and i != index):
            t = t.get_next()
            i += 1
        if(t == None):
            self.append(n)
            return True

        n.set_pre(t)        
        n.set_next(t.get_next())
        t.get_next().set_pre(n)
        t.set_next(n)

        return True

    def reverse(self):
        self.last = t = self.first
        while(t != None):
            next = t.get_next()
            t.set_next(t.get_pre())
            t.set_pre(next)
            t = next
            if(t != None and t.get_next() == None):
                self.first = t

    def append(self, node):
        if(self.first == self.last == None):
            self.last = self.first = node
            return
        node.set_pre(self.last)
        self.last.set_next(node)
        self.last = node

    def display(self):
        t = self.first
        while(t != None):
            print(t.data)
            t = t.get_next()
