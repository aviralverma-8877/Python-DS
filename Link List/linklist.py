import gc

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def get_next(self):
        return self.next
    def get_data(self):
        return self.data
    def set_next(self, node):
        self.next = node
    def set_data(self, data):
        self.data = data

class StackedList:
    def __init__(self):
        self.head = None
    
    def prepend_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def append_node(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return

        tmp = self.head
        while(tmp.get_next() != None):
            tmp = tmp.get_next()        
        tmp.set_next(new_node)

    def add_node_sorted(self, data):
        new_node = Node(data)

        if(self.head == None):
            self.head = new_node
            return

        if(self.head.get_data() >= data):
            new_node.set_next(self.head)
            self.head = new_node
            return

        h = self.head
        t = None

        while(h != None and h.get_data() < data):
            t = h
            h = h.get_next()
        
        new_node.set_next(t.get_next())
        t.set_next(new_node)

    def list_count(self):
        node = self.head
        count = 0
        while(node != None):
            node = node.get_next()
            count += 1
        return count

    def list_print(self):
        node = self.head
        while(node != None):
            print(node.get_data(), end=" ")
            node = node.get_next()
        print("")
    
    def list_count_rec(self, n):
        if(n == None):
            return 0
        else:
            return self.list_count_rec(n.get_next()) + 1
    
    def list_print_rec(self, n):
        if(n != None):
            print(n.get_data(), end=" ")
            self.list_print_rec(n.get_next())            
        
    def list_reverse(self):
        p = self.head
        q = None
        r = None
        while(p != None):
            r = q
            q = p
            p = p.get_next()
            q.set_next(r)
        self.head = q

    def list_reverse_rec(self,q,p):
        if(p != None):
            self.list_reverse_rec(p,p.get_next())
            p.set_next(q)
        else:
            self.head = q
            
    def delete_node(self, index):
        node = self.head
        pre_node = None
        i = 0
        while(i != index):
            pre_node = node
            node = node.get_next()
            i += 1
        pre_node.set_next(node.get_next())
        del node
        gc.collect()
    
    