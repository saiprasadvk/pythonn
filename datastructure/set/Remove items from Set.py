Remove items from Set

Ans::

S = [12, 10, 13, 15, 8, 9]

def remove(S):
    while S:
        S.pop()
        print(S)
        
remove(set(S))  

O/P::
{9, 10, 12, 13, 15}
{10, 12, 13, 15}
{12, 13, 15}
{13, 15}
{15}
set()
