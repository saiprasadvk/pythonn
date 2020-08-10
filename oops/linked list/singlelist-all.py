class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
     
    def add(self,newval):
        newdata = Node(newval)
        newdata.next = self.head
        self.head = newdata
        
    def Delete(self,rmdata):
        
        headval = self.head
        
        if headval is not None:
            if (headval.data == rmdata):
                self.head = headval.next
                headval = None
                return
        
        while headval is not None:
            print("hello",headval.data)
            if (headval.data == rmdata):
                break
            prev = headval
            headval = headval.next
        
        if (headval == None):
            print("Values is not present")
            return
         
        prev.next = headval.next
        
        headval = None
        
    def Insert(self,newdata):
        New = Node(newdata)
        New.next = self.head
        self.head = New
            
    def link(self):
        val = self.head
        while val:
            print(val.data)
            val = val.next


m = linkedlist()
n = [2,3,4,5]

for i in n:
    m.add(i)

m.Insert(7)

m.Delete(5)

m.link()
    
O/P::
hello r
hello 5
r
4
3
2
    
