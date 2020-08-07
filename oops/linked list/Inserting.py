#Inserting at the Beginning of the Linked List

class Node:
    def __init__(self,test = None):
        self.test = test
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def linklist(self):
        link = self.head
        while link is not None:
            print(link.test)
            link = link.next
            
    def Atstart(self,newdata):
        New = Node(newdata) 

        New.next = self.head
        self.head = New
        
l = Linkedlist()
l.head = Node('1')
l2 = Node("2")
l3 = Node("3")

l.head.next = l2
l2.next = l3

l.Atstart('0')

l.linklist()

O/P::

0
1
2
3
