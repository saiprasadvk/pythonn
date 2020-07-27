#Generate two output strings depending upon occurrence of character in input string in Python
Input : str = "geeksforgeeks"
Output : String with characters occurring once:
"for".
String with characters occurring multiple times:
"egks"

Ans::

Str = input("Enter the string:")

Dict = {}
a = ""
b = ""

for x in Str:
    Dict[x] = Str.count(x)    #can use this to find the count "from collections import Counter"  

for m,n in Dict.items():
    if n % 2 == 0:
        a = a + m
    elif n % 2 == 1:
        b = b + m
        
print(a)
print(b)

O/P:

paizwlc
