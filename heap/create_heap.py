class Solution:
    def __init__(self) -> None:
        self.heap = [0]
    
    def insert(self, ele):
        if len(self.heap) == 0:
            self.heap.append(ele)
            return
        self.heap.append(ele)
        child_index = len(self.heap)-1
        while(child_index > 1):
            parent_index = int(child_index/2)
            if self.heap[parent_index] < self.heap[child_index]:
                temp = self.heap[child_index]
                self.heap[child_index] = self.heap[parent_index]
                self.heap[parent_index] = temp
            else:
                break
            child_index = parent_index

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            ele = self.heap.pop(0)
            return ele
        first_ele = self.heap[1]
        last_ele = self.heap.pop()
        self.heap[1] = last_ele
        parent_index = 1
        while(True):
            left_child_index = parent_index*2
            right_child_index = (parent_index*2)+1
            considered_child = None
            if left_child_index > (len(self.heap)-1):
                break
            elif right_child_index > (len(self.heap)-1):
                considered_child = left_child_index
            else:
                if self.heap[left_child_index] > self.heap[right_child_index]:
                    considered_child = left_child_index
                else:
                    considered_child = right_child_index
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[considered_child]
            self.heap[considered_child] = temp
            parent_index = considered_child
        return first_ele

    def print_heap(self):
        print(self.heap)


s = Solution()
s.insert(12)
s.insert(15)
s.insert(12)
s.insert(10)
s.insert(7)
s.insert(22)
s.insert(34)
s.insert(1)
s.insert(2)
s.print_heap()
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())
print(s.delete())