3. Form a palindrome string from the input (Which is missed in last set)
    * Do not use any inbuilt functionality
  i/o : aabbc
  o/p : abcba (any of the possible palindrome)

  i/o : sdab
  o/p : can not form palindrome
  
Ans::
Sol 1::
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

Sol2::
      
print("Enter any string: ")
x = input()
d = {}

for i in x:
    if i not in d:
        d[i] = x.count(i)

ns= ""
flag = True
invalid = False

for k,v in d.items():
    if v%2 == 0:
        ns = k*(v//2) + ns + k*(v//2)
        print("ns is:",ns)
    else:
        if not flag:
            print("not ns is:",ns)
            print("Invalid")
            invalid = True
            break
            
        ns = ns[:len(ns)//2] + k*v + ns[len(ns)//2:]
        flag = False
            
        if not invalid:
            print("pallindrom is:",ns)
            
 O/p:
   Enter any string: 
      aabbc
   pallindrom is: bacab   

