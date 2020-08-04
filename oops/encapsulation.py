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
