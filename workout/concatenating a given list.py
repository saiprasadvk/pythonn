Python program to create a list by concatenating a given list

Sol 1::

def concatenating(L):
    new_list = []

    for y in range(1, n):
        for x in my_list:
            new_list.append(x+str(y))
    return new_list
    
L = ['p', 'q']
n = 5
concatenating(L)

O/P::

['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4']
