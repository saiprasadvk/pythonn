Program to accept the strings which contains all vowels

Ans:

def string(Str):
    v = ['a','e','i','o','u']
    L = [x for x in Str]
    V = [x for x in set(L) if x in v]
    print(V)
    
    if len(v) == len(V):
        print("accept the strings ")
    else:
        print("can't accept the strings ")

Str = input("Enter the string:")
string(Str)        

O/p:
Enter the string:geeksfoegrrks
['o', 'e']
can't accept the strings 
