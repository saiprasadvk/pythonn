Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

Ans::

L = ['abc', 'xyz', 'aba', '1221','323']
count = []
for i in L:
    for j in i:
        if i[0] == i[-1]:
            count.append(i)
len(set(count)) 

O/P:

3
