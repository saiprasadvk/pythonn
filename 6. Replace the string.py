6. Search and replace the string 
  - Should not use "replace" functionalitie i/o 
  - "Python Programming"   search_char = "P" Relace_char = "B o/p - Bython Brogramming
  
Ans::
  
I = "Python Programming"
O = ""
for x in I:
    if x == 'P':
        O += "B"
    else:
        O += str(x)

print(O)


O/P:

Bython Brogramming
