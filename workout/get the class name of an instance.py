Write a Python program to get the class name of an instance in Python.

Ans::

import itertools
x = itertools.cycle('ABCD')
print(type(x).__name__)


O/P::

cycle
