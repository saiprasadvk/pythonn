8. Print the each character along with that index in a string i/o - "Python" o/p - P-0 y-1 t-2 h-3 o-4 n-5


Ans:
sol1:
    
I = "Python"

for x in range(len(I)):
    a = I[x]
    print('{}-{}'.format(a,x))
    
sol2:
    
list_enumerate = list(enumerate(I))

for i in list_enumerate:
        print(i)
    
O/P:


P-0
y-1
t-2
h-3
o-4
n-5
