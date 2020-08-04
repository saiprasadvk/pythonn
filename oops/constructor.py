class Number():
    def __init__(self,i = 0, j = 1):
        self.i = i
        self.j = j
        print("i is ",self.i, "\nj is ",self.j)
        
    def fun(self):
        return (f'{self.i} + {self.j}k')
    
obj = Number() 
print(obj.fun(),'\n')

obj = Number(5,7)
print(obj.fun(),'\n')

obj = Number(5)
print(obj.fun())


O/P::
i is  0 
j is  1
0 + 1k 

i is  5 
j is  7
5 + 7k 

i is  5 
j is  1
5 + 1k
