7. Remove the character from odd index in a string 
i/o - "Python" o/p - "yhn"


Ans:

I = "Python"
O = ""

for i in range(1,len(I)+1):
    if i % 2 == 0:
        O += str(I[i-1])
        
print(O)

O/P:

yhn
