3. Form a palindrome string from the input (Which is missed in last set)
    * Do not use any inbuilt functionality
  i/o : aabbc
  o/p : abcba (any of the possible palindrome)

  i/o : sdab
  o/p : can not form palindrome
  
Ans::
a = input("Enter the string:")

b = []

for i in range (len(a)):
    if a[i] not in b:
        b.append(a[i])
        #print("add",b)
    else:
        b.remove(a[i])
        #print("remove",b)
        
if (len(a)% 2 == 0 and len(b) == 0 or (len(a) % 2 == 1 and len(b) == 1)): 
    print(a)
else:
    print('can not form palindrome')
    
o/p:
Enter the string:abab
abab
