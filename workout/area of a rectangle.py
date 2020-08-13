Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle?

Ans::

class rectangle:
    def __init__(self):
        self.length = ''
        self.width = ''
    
    def getvalues(self):
        self.length = int(input("Enter value of length : "))
        self.width = int(input("Enter value of width : "))
    
    def area(self):
        a = self.length * self.width
        print("Area of Rectangel is",a)
        
def calc():
    a = rectangle()
    a.getvalues()
    a.area()
    
if __name__ == "__main__":
    calc()
    
 O/P::

Enter value of length : 5
Enter value of width : 4
Area of Rectangel is 20
