Write a Python function that takes a number as a parameter and check the number is prime or not.

Ans::

def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
        return True
    
def main():
    n = int(input("Enter the number:"))
    a = prime(n)
    print(a)

if __name__ == '__main__':
    main()
    
    
O/P::

Enter the number:5
True
