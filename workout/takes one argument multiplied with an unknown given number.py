Create a function that takes one argument multiplied with an unknown given number

Ans::

def func(n):
    return lambda x : x * n


a = func(2)
print("Double the number=", a(15))


O/P::

Double the number= 30
