class Node:
    def __init__(self,test = None):
        self.test = test
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def atmiddle(self,middle,newdata):
        Newnode = Node(newdata)
        if middle is None:
            print("Data is not present")
            return
        Newnode.next = middle.next
        middle.next = Newnode
     
    def linklist(self):
        link = self.head
        while link is not None:
            print(link.test) 
            link = link.next

l = Linkedlist()
l.head = Node("1")
l2 = Node("2")
l3 = Node("3")


l.head.next = l2

l.atmiddle(l.head,"5")

l2.next = l3

#l.atmiddle(l.head.next,"5")

l.linklist()


O/P::

1
5
2
3
