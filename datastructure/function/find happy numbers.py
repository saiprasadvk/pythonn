#Python program to print all happy numbers between 1 and 100

Ans::
def isHappyNumber(num):
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;

#Displays all happy numbers between 1 and 100    
print("List of happy numbers between 1 and 100: ")    
for i in range(1, 101):    
    result = i
    while(result != 1 and result != 4):    
        result = isHappyNumber(result)
        
    if(result == 1):    
        print(i,end=' ')
        
O/P:

List of happy numbers between 1 and 100: 
1 7 10 13 19 23 28 31 32 44 49 68 70 79 82 86 91 94 97 100
