Count occurrences of an element in a Tuple

Tuple: (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

Ans::

T = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

Input = int(input("Enter the number:"))
count = 0

for i in T:
    if Input == i:
        count += 1
        
print(count,'time')        

O/P:

Enter the number:4
0 time
