 Python program to find the missing and additional elements 
 Ans::
 
 list1 = [1, 2, 3, 4, 5, 6] 
 list2 = [4, 5, 6, 7, 8] 
 
 
# prints the missing and additional elements in list2 
print("Missing values in second list:", (set(list1).difference(list2))) 
print("Additional values in second list:", (set(list2).difference(list1))) 

# prints the missing and additional elements in list1 
print("Missing values in first list:", (set(list2).difference(list1))) 
print("Additional values in first list:", (set(list1).difference(list2)))

O/P:
Missing values in second list: {1, 2, 3}
Additional values in second list: {7, 8}
Missing values in first list: {7, 8}
Additional values in first list: {1, 2, 3}
