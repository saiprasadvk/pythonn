12. swap the string and make it as a palindrom. i/o - abacb o/p - abcba i/o - aabc o/p - Invalid


Ans::

Str = input("Enter the string:")
new_str = [] 
    
for i in range(len(Str)):
    if (Str[i] in new_str):
        new_str.remove(Str[i]) 
    else:
        new_str.append(Str[i])
        
print(new_str)
print(len(Str))
print(len(new_str))
        
if (len(Str)% 2 == 0 and len(new_str) == 0 or (len(Str) % 2 == 1 and len(new_str) == 1)): 
    print(Str)
else:
    print('invalid')

O/P::

Enter the string:avaad
['v', 'a', 'd']
5
3
invalid   
    
    
