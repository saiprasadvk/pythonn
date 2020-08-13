Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

Ans::

class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def perimeter(self):
        a = 3.14*(self.radius)**2
        print("Area of a circle",a)
        
    def area(self):
        b = 2*3.14*self.radius
        print("perimeter of a circle",b)
        
def main():
    a = circle(3)
    a.area()
    a.perimeter()

if __name__ == "__main__":
    main()
    
 O/P::
 
 
perimeter of a circle 18.84
Area of a circle 28.26
