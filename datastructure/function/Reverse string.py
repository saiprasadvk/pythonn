Write a Python program to reverse a string.

Ans::

def reverse(s):
    Str = ""
    for i in s:
        Str = i + Str
    return Str

L = "1234abcd"
reverse(L)

O/p::

dcba4321
