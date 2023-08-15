class Person:
    #construct methods
    def __init__(self,name,surname,year):

        #object attributes
        self.name=name
        self.surname=surname
        self.year=year
    
    #instance methods
    def intro(self):
        return f"My name {self.name} and Surname {self.surname}"

    def calculate_age(self):
        return f"{2023-self.year}"
        
#Object,Instance
p1=Person("Jack","Sparrow",2004)
p2=Person("Mary","Elisabeth",2002)

print(p1.intro())
print(p2.intro())

print(p1.calculate_age())
print(p2.calculate_age())

