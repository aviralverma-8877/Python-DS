class SelectionSort:
    def __init__(self, arr):
        self.arr = arr
    
    def selection_sort(self):
        for i in range(0, len(self.arr)-1):
            m = None
            index = 0
            for j in range(i+1, len(self.arr)):
                if m == None or m > self.arr[j]:
                    m = self.arr[j]
                    index = j
            t = self.arr[i]
            self.arr[i] = self.arr[index]
            self.arr[index] = t
    
    def display(self):
        print(self.arr)

s = SelectionSort([9,5,3,4,6,8])
s.selection_sort()
s.display()