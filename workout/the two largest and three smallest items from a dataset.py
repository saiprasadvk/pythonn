Write a Python program to get the two largest and three smallest items from a dataset.

Sol::

import heapq
h = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
print(heapq.nlargest(2,h))
print(heapq.nsmallest(3,h))

O/P::
[100, 90]
[10, 20, 20]
