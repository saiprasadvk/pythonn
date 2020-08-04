class test():
    "Hello this is for doc statment"
    b = 30
    
    def fun():
        "This is defining the function"
        print("Hai")

##before assign the the object  
print(test.b)
test.fun()

        
#After assign the the object        
obj = test
print(obj.__doc__)
print(obj.b)
obj.fun()

O/P:

30
Hai
Hello this is for doc statment
30
Hai
