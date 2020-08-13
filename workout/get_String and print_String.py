1.Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case?

Ans::

class string:
    def __init__(self):
        self.str1 = ""
        
    def getstr(self):
        self.Str = input("Enter the string:")
        
    def printstr(self):
        print(self.Str.upper())

def main():
    a = string()
    a.getstr()
    a.printstr()
    
if __name__ == "__main__":
    main()
    
O/P::

Enter the string:sai prasad
SAI PRASAD
