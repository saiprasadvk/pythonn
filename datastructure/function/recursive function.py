Write a recursive function to calculate the sum of numbers from 0 to 10
Sol 1::

def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(res)

Sol2::
def Add(n):
    count = 0
    for i in range(n+1):
        count += i
    return count
    
Add(10)

O/P:

55
    
