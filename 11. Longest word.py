11. Find the longest word from the sentense i/o - "This is the sample string program" o/p - "program" - 7 (longest word)

Ans::
sol1::
        
I = "This is the sample string program"

m = I.split()
n = []

for x in m:
    a = len(x)
    n.append(len(x))
    n.sort()

for y in m:
    if n[-1] == len(y):
        print(y)
        
sol2:
I = "This is the sample string program"

m = I.split()

max_len = -1

for ele in m:
    if len(ele) > max_len:
        max_len = len(ele)
        long = ele 

print("The longest word is : ", long) 

   
        
O/P:

program
