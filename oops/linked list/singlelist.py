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
