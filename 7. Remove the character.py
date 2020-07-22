7. Remove the character from odd index in a string 
i/o - "Python" o/p - "yhn"


Ans:
Sol1::
I = "Python"
O = ""

for i in range(1,len(I)+1):
    if i % 2 == 0:
        O += str(I[i-1])
        
print(O)

Sol2::
        
I = "Python"
I[1::2]

O/P:

yhn
