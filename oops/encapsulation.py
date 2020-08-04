1)
class seeme:
    def public(self):
        return "You can see me"
        
    def __private(self):
        return "you cann't see me"

a = seeme()    
print(a.public())
print(a._seeme__private())

O/P::
You can see me
you cann't see me

2)

class Robot(object):
    def __init__(self):
        self.a = 123
        self._b = 123
        self.__c = 123

obj = Robot()
print(obj.a)
print(obj._b)
print(obj._Robot__c)

O/P::
123
123
123

3)
class Base:
    def __init__(self):
        self.__a = 45
        print("Started")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ") 
        print(self._Base__a)
            

obj1 = Base()
print(obj1._Base__a)

obj2 = Derived()

O/P::
Started
45
Started
Calling protected member of base class: 
45
