class Card:
    def __init__(self,type,value):
        self.type=type
        self.value=value

    #def Bringcard(self):
    #  return f"{self.type} {self.value}"

    def __repr__(self):
        return f"{self.type}{self.value}"
    
red5=Card("red","5")     
green4=Card("green","4")

#print(red5.Bringcard())
#print(green4.Bringcard())

print(red5)
print(green4)




        