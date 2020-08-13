Write a Python program to compare two unordered lists

Ans1::

n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]

d1 = dict()
d2 = dict()

for i in n1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
        
for j in n2:
    if j in d2:
        d2[j] += 1
    else:
        d2[j] = 1    
        
if d1 == d2:
    print("True")
else:
    print("False")
    
Ans2::
from collections import Counter
def compare_lists(x, y):
    return Counter(x) == Counter(y)
n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
print(compare_lists(n1, n2))
