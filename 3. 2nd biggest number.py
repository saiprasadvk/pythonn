3. Find the 2nd biggest number from the list 
  - I/o will be non sequence without sorting need to find the number 
  - Dont use inbuild functionality 
  - can use any looping functionality i/o - [20,10,23,50,600,300] o/p - 300
  
Ans::
Sol1:    
    
I = [20,10,23,50,600,300]

for i in range(len(I)):
    for j in range(i + 1, len(I)):
        if I[i] < I[j]:
            I[i], I[j] = I[j], I[i]

print(I[1])

Sol2:
  
I = [20,10,23,50,600,300]
temp = set(I) 
temp.remove(max(temp))
print(max(temp)) 

sol3:
  
I = [20,10,23,50,600,300]

first = second = I[0]

for j in range(1, len(I)):
    if(I[j] > first):
        second = first
        first = I[j]
    elif(I[j] > second and I[j] < first):
        second = I[j]
        
print("The 2nd big number is : ", second)  

O/p::

300
  
