6. Search and replace the string 
  - Should not use "replace" functionalitie i/o 
  - "Python Programming"   search_char = "P" Relace_char = "B o/p - Bython Brogramming
  
Ans::
Sol1::  
I = "Python Programming"
O = ""
for x in I:
    if x == 'P':
        O += "B"
    else:
        O += str(x)

print(O)

Sol2::
I = "Python Programming"
string = list(I)
result = []
for i in string:
        if i == 'P':
                i = 'B'
        result.append(i)

print(''.join(result))    


O/P:

Bython Brogramming
