1.Get all the numbers inbetween two numbers in the list
      -Input should read from user (start & end values)
      -Slicing methodalogy can use i/o - list = [1,2,3,4,5,5,6,10,20,40] Start - 5 End - 20 o/p [5,5,6,10,20]
      
      
Ans::

List = [1,2,3,4,5,5,6,10,20,40]

Start = int(input("Enter the start value:"))
End = int(input("Enter the end value:"))

print(List[Start:End])

O/p:

Enter the start value:5
Enter the end value:20
[5, 6, 10, 20, 40]
