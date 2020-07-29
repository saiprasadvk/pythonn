Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'

Ans::

def Case(c):
    U = 0
    L = 0
    for i in c:
        if i.lower() == i:
            L += 1
        elif i.upper() == i:
            U += 1
        elif i == None:
            pass
        
    print("upper case is:",U)
    print("Lower case is:",L)
 
c = 'The quick Brow Fox'
d = c.replace(" ", "")
Case(d)

O/P::

upper case is: 3
Lower case is: 12
