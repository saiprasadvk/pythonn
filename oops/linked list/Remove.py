class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def remove(self,rmdata):
        
        headval = self.head
        
        if headval is not None:
            if (headval.data == rmdata):
                self.head = headval.next
                headval = None
                return
            
        while headval is not None:
            if (headval.data == rmdata):
                break
            prev = headval
            headval = headval.next
             
        if (headval == None):
            print("Values is not present")
            return
        
        prev.next = headval.next

        headval = None
       
    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode        
        
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
            
    
l = SLinkedList()

l.head = Node('1')

l2 = Node('2')
l3 = Node('3')
l4 = Node('4')

l.head.next = l2
l2.next = l3
l3.next = l4

l.Atbegining('0')

l.remove('3')

l.LListprint()

O/P::

0
1
2
4
