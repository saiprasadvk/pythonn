1. Find the missing numbers in between
i/o : [1,2,10,12]
o/p : [3,4,5,6,7,8,9,11]

Ans::

I = [1,2,10,12]

I1 = []

for x in range(1,12):
    if x not in I:
        I1.append(x)

print(I1)

O/p:
[3,4,5,6,7,8,9,11]

