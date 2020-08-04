class Name(object):
    def __init__(self):
        self.msg = None

    def setter(self,Str):
        self.msg = Str
        
    def getter(self):
        print(self.msg)
    
def main():
    M = Name() 
    M.getter()

    M.setter('vika')
    M.getter()

if __name__ == '__main__':
    main()
    
    
O/P::
None
vika
