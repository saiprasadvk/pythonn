class Number():
    def __init__(self,i = 5, j = 1):
        self.i = i
        self.j = j
        print("i is ",self.i, "\nj is ",self.j)
        
    def fun(self):
        return (f'{self.i} + {self.j}k')
    
obj = Number() 
print(obj.fun())
print(obj.i)

O/P::
i is  5 
j is  1
5 + 1k
5

Deleting::
1)
del obj.i
print(obj.i)

O/P:
AttributeError: 'Number' object has no attribute 'i'

2)
del obj
print(obj.fun())

O/P:

NameError: name 'obj' is not defined

3)
del Number.fun
print(obj.fun())

O/P::
AttributeError: 'Number' object has no attribute 'i'
