Count the elements in a list until an element is a Tuple

Ans::
Sol1::
#I = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
I = [4, (5, 6), 10, (1, 2, 3), 11, 2, 4]

element = 0
for x in I:
    if type(x) == str:
        element += 1
    elif type(x) == tuple:
        print(I.index(x))
        break
Sol2::
        
element=0

for x in I:
    if type(x) is tuple:
        break
    element+=1    
    
    
print(element)
        
        
O/P::

1
