4. There is two list, Find common values in both the list - Type conversion can use - Not required to use any loops i/o - [1,2,3], [2,3,4] o/p - [2,3]


Ans:

I1 = [1,2,3]
I2 = [2,3,4]

s1 = set(I1)
s2 = set(I2)

print(list(s1.intersection(s2)))

O/P:

[2, 3]
