
# card type=> green,blue,yellow,red
# card value=> 1,2,3,4,5,6,7,8,9,10

from random import shuffle

class Card3:
    def __init__(self,type,value):
        self.type=type
        self.value=value

    def __repr__(self):
        return f"{self.type}{self.value}"

class Allcards:
    def __init__(self):
        type=["green","blue","yellow","red"]
        value=["1","2","3","4","5","6","7","8","9","10"]
        self.cards=[Card3(type,value) for type in Allcards.types for value in Allcards.values]
        #for type in types:
        #    for value in values:
        #        self.cards.append(Card2(type,value))
        
    def CardNumbers(self):
        return len(self.cards)
        
    def cardcrowd(self):
        if(self.CardNumbers()<52):
            return ValueError("Cards can crowd")
        shuffle(self.cards)
    
    def cardBring(self,value):
        cardNumber=self.CardNumbers()
        if cardNumber==0:
            raise ValueError("All cards crowded.")
        value=min([cardNumber,value])
        cards=self.cards[-value:]
        self.cards=self.cards[:-value]
        return cards
        
        #print(self.cards)

allcard=Allcards()

result=allcard.CardNumbers()
allcard.cardcrowd()
result=allcard.cards

allcard.cardcrowd(53)
print(allcard.CardNumbers())

print(allcard.cards)






