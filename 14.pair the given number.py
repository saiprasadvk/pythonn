2. Find the pair which sum is equal to given number
i/o : list1 = [1,2,3,4...10]
 sum = 10
o/p : [(2,8),(4,6),(1,9)...]

Ans::
list1 = [1,2,3,4,5,6,7,8,9,10]
Sum = 10
list2 = []
for x in range (len(list1)):
    a = list1[x]
    b = Sum - a
    if b in list1:
        list2.append((a,b))
        
print(list2)

O/p::
[(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]
