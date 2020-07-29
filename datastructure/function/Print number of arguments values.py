Write a function func1() such that it can accept a variable length of  argument and print all arguments value

Ans::

def func1(*arg):
    for i in arg:
        print(i)
        
func1("hello","world","All good")

O/P:

hello
world
All good
