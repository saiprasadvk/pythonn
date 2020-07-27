#Reversing a Tuple

Input : tuples = ('z','a','d','f','g','e','e','k')

Ans::

t = ('z','a','d','f','g','e','e','k')

l = []

for i in list(t):
    l.insert(0,i)
    
print(tuple(l))

O/P::
('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
