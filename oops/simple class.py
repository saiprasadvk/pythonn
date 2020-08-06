import datetime

class person:
    def __init__(self,name,birthdate,address,email):
        self.name = name
        self.birthdate = birthdate
        self.address = address
        self.email = email
            
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        
        return age    
    
Age = person('hari',datetime.date(1992, 3, 12), 'maldevis', 'hari@mail.com')

print(Age.name)
print(Age.email)
print(Age.age())

O/P:
hari
hari@mail.com
28 
