 Python program to generate squares from 1  to 100 using yield and therefore generator 
 
Ans:: 
def Square():
        i = 1 
        while True:
            yield i*i
            i += 1

for num in Square():
    if num > 100:
        break
    print(num)    
    
O/P:

1
4
9
16
25
36
49
64
81
100
