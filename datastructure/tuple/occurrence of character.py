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
    if n  == 1:
        a = a + m
    elif n > 1:
        b = b + m
        
print("single",a)
print("multi",b)

Sol 2:: 
        
a = ''
b = ''

for x in Str:
    if Str.count(x) == 1:
        a = a + x
    elif Str.count(x) > 1:
        if x not in b:
            b = b + x

print("single",a)
print("multi",b)
                      
   
O/P:

paizwlc
