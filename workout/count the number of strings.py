Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

Ans::
Sol1:: 

L = ['abc', 'xyz', 'aba', '1221','323']
count = []
for i in L:
    for j in i:
        if i[0] == i[-1]:
            count.append(i)
len(set(count)) 

Sol2:: 
        
count = 0
for j in L:
    if j[0] == j[-1]:
        count += 1
count 

O/P:

3
