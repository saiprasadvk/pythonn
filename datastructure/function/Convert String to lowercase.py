# Python Program to Convert String to lowercase by using ASCII

Ans::

def Str(N):
    n = ''
    for i in N:
        if i >= 'A' and i <= 'Z':
            n = n + (chr(ord(i)+32))
        else:
            n = n + i
    print("The Orginal string is:",N)        
    print("The lowercase string is:",n)
    
N = "Sai PraSAd"
Str(N)    

O/P:

The Orginal string is: Sai PraSAd
The lowercase string is: sai prasad
