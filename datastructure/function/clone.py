# Python code to clone or copy a list 

Ans::

def clone(c):
    afertclone = []
    afertclone.extend(c)
    return afertclone
    
c = [1,2,3,45]
d = clone(c)

print("Before clone is :",c)
print("After clone is :",d)

O/P::

Original List: [4, 8, 2, 10, 15, 18]
After Cloning: [4, 8, 2, 10, 15, 18]
