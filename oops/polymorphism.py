class Parrot:
    a = 6
    b = 8
    def fly(self):
        print("Parrot can fly",self.a+ self.b)
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#Object

blu = Parrot()
peggy = Penguin()

#calling
flying_test(blu)
flying_test(peggy)

O/P::
Parrot can fly 14
Penguin can't fly
