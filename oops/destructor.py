class school:
    def __init__(self):
        self.ids = 0
        self.name = ""
        self.gender = ""
        self.city = ""
        self.std = 0
        print("Object Started")
        
    def __del__(self):   
        print("Object Destroyed")
    
    def setdetails(self):
        self.ids = int(input("Enter id:"))
        self.name = input("Enter name:")
        self.gender = input("Enter gender:")
        self.city = input("Enter city:")
        self.std = int(input("Enter std:"))
        
    def showdetails(self):
        print("Enter Id :",self.ids)
        print("Enter name :",self.name)
        print("Enter gender :",self.gender)
        print("Enter city :",self.city)
        print("Enter std :",self.std)

def main():
    M = school()
    M.setdetails()
    M.showdetails()

if __name__=="__main__":
    main()
    
    
O/P::

Object Started
Enter id:45
Enter name:nun
Enter gender:m
Enter city:toyo
Enter std:9
Enter Id : 45
Enter name : nun
Enter gender : m
Enter city : toyo
Enter std : 9
Object Destroyed

