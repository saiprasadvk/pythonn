Given a string, count the number of vowels present in given string using Sets.

Ans::

I = 'GeeksforGeeks'

m =  I.lower()
v = set("aeiou")

count = 0

for i in m:
    if i in v:
        count += 1 
    else:
        pass
print(count)    

O/P:
5
