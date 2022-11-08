class BubbleSort:
    def __init__(self, l) -> None:
        self.l = l
    
    def bubble_sort(self):
        if (len(self.l)>0):
            for i in range(0, len(self.l)):
                swaping = False
                for j in range(0, len(self.l)-1-i):
                    if(self.l[j]>self.l[j+1]):
                        swaping = True
                        (self.l[j], self.l[j+1]) = self.swap(self.l[j], self.l[j+1])
                if not swaping:
                    break
    
    def swap(self, m, n):
        t = m
        m = n
        n = t
        return (m, n)

    def display(self):
        for j in self.l:
            print(j)

sort = BubbleSort([6,3,8,5,2,9,1])
sort.bubble_sort()
sort.display()