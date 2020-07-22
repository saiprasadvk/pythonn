11. Find the longest word from the sentense i/o - "This is the sample string program" o/p - "program" - 7 (longest word)

Ans::

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
        
O/P:

program
