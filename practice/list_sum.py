# https://leetcode.com/problems/add-two-numbers/submissions/
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
#  10000001 + 465 = 000466
# [5,6,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = self.list_to_int(l1)
        num2 = self.list_to_int(l2)
        sum = num1+num2
        return(self.int_to_list(sum))
    
    def int_to_list(self, i):
        head = None
        if i==0:
            head = ListNode()
        t = head
        while(i>0):
            r = int(i % 10)
            i = int((i - r) / 10)
            if(head == None):
                head = ListNode(val=r, next=None)
                t = head
            else:
                while(t.next != None):
                    t = t.next
                t.next = ListNode(val=r, next=None)
        return head

    def list_to_int(self,l):
        stack = []
        t = l
        while(t != None):
            stack.append(t.val)
            t = t.next
        mul = 1
        num = 0
        for i in stack:
            num += i*mul
            mul = mul * 10
        return num
    
    def print_list(self,l):
        t = l
        while(t != None):
            print(t.val, end=" ")
            t = t.next
        print()

s = Solution()
l1 = s.int_to_list(1000000000000000000000000000466)
s.print_list(l1)