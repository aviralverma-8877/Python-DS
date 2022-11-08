class InsertionSort:
    def __init__(self, l) -> None:
        self.l = l
    
    def insertion_sort(self):
        for i in range(1, len(self.l)):
            j = i-1
            x = self.l[i]
            while(j>-1 and self.l[j]>x):
                self.l[j+1] = self.l[j]
                j -= 1
            self.l[j+1] = x
        return self.l

    def display(self):
        for j in self.l:
            print(j)

sort = InsertionSort([6,3,8,5,2,9,1])
sort.insertion_sort()
sort.display()