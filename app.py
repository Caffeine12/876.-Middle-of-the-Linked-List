class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBegin(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            new_node.next = None
            return
        else:
            new_node.next = self.head
            self.head = new_node
            return
        
    def printll(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

class Solution(object):
    def middleNode(self, head):
        count = 0
        current = head
        while current:
            count+=1
            current = current.next
        current = head
        for i in range(1,(count//2)+1):
            current = current.next
        return current



myll = LinkedList()

for i in range(0,4):
    input_value = int(input())
    myll.insertAtBegin(input_value)

# myll.printll()

mysol = Solution()
middle = mysol.middleNode(myll.head)
print(f"Middle is: {middle.val}")