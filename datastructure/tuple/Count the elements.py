Count the elements in a list until an element is a Tuple

Ans::

#I = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
I = [4, (5, 6), 10, (1, 2, 3), 11, 2, 4]

element = 0
for x in I:
    if type(x) == str:
        element += 1
    elif type(x) == tuple:
        print(I.index(x))
        break
    
O/P::

1
