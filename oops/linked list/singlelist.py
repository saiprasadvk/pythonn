Sol1:
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def linklist(self):
        test = self.head
        while test is not None:
            print(test.data)
            test = test.next

l = Linkedlist()
l.head = Node("1")

l2 = Node('2')
l3 = Node('3')

l.head.next = l2

l2.next = l3

l.linklist()


O/P::

1
2
3



Sol2::
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def push(self,newval):
        newnode = Node(newval)
        newnode.next = self.head
        self.head = newnode
        
    def link(self):
        test = self.head
        while test is not None:
            print(test.data)
            test = test.next
            
m = Linkedlist()
n = [1,2,3,4]

for i in n:
    m.push(i)
m.link()

O/P::
4
3
2
1        
        
