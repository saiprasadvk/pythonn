class Node:
    def __init__(self,data = None):
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
        
        while headval is not None:
            print("hello",headval.data)
            if (headval.data == rmdata):
                break
            prev = headval
            headval = headval.next
            
        if (headval == None):
            print("given remove data is not there")
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
        

p = linkedlist()
n = [2,3,4,5]

for i in n:
    p.add(i)
    
p.Insert('r')

p.Delete(5)

p.link()
    
O/P::
hello r
hello 5
r
4
3
2
    
