Pairs of complete strings in two sets

Ans::

set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc'] 
set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz'] 
count = 0

for i in set1:
    for j in set2:
        m = i + j
        tmpSet = []
        for ch in m:
            if (ord(ch)>=ord('a') and ord(ch)<=ord('z')):
                tmpSet.append(ch)
            
        if len(set(tmpSet)) == 26:
            count = count + 1
            
print(count)

O/P::

7


