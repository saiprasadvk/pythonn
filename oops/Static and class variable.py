class student:
    College = 'Engineering'
    
    def __init__(self,name,major):
        self.name = name
        self.major = major
        
a = student('hari','ece')

print(a.College)
print(a.name)
print(a.major)

O/P::
Engineering
hari
ece
