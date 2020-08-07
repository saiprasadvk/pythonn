class Node:
    def __init__(self,test = None):
        self.test = test
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def Atend(self,newdata):
        Newnode = Node(newdata)
        if self.head is None:
            self.head = Newnode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = Newnode
        
    def linklist(self):
        link = self.head
        while link is not None:
            print(link.test)
            link = link.next
            
l = Linkedlist()
l.head = Node('1')
l2 = Node("2")
l3 = Node("3")

l.head.next = l2
l2.next = l3

l.Atend('4')

l.linklist()

O/P::
1
2
3
4
