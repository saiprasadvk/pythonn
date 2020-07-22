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

O/p::

300
  
