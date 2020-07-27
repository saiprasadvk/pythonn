Function to find lost element from a duplicate array 
Ans::
A = [1, 4, 5, 7, 9]
B = [4, 5, 7]

set1 = set(A)
set2 = set(B)

if len(A) > len(B):
    print(list(set1-set2),"is missing from second array.")
elif len(A) < len(B):
    print(list(set2-set1),"is missing from first array.")
    
O/P::
 [1, 9] is missing from second array.
