8. Print the each character along with that index in a string i/o - "Python" o/p - P-0 y-1 t-2 h-3 o-4 n-5


Ans:

I = "Python"

for x in range(len(I)):
    a = I[x]
    print('{}-{}'.format(a,x))
    
O/P:


P-0
y-1
t-2
h-3
o-4
n-5
