Sol1::
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

# Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        
        
# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

l = doubly_linked_list()
l.head = Node('1')

l2 = Node('2')
l3 = Node('3')

l.head.next = l2
l2.next  = l3

l.push('14')
l.push('13')
l.push('12')

l.listprint(l.head)

O/P:

12
13
14
1
2
3



Sol2::
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

# Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        
        
# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next


n = doubly_linked_list()
m = [14,13,12]

for i in m:
    n.push(i)
n.listprint(n.head)


O/P::
12
13
14
