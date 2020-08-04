class Bird:
    def __init__(self):
        print("Its is bird")
    def whatisthis(self):
        print("bird")
    def swim(self):
        print("Swim faster")
        
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Its is Penguin")
    def whatisthis(self):
        print("penguin")
    def run(self):
        print("Run faster")

a = Bird()
a.whatisthis()
a.swim()
print()
b = Penguin()
b.whatisthis()
b.swim()
b.run()

O/P::

Its is bird
bird
Swim faster

Its is bird
Its is Penguin
penguin
Swim faster
Run faster
