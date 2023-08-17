
# card type=> green,blue,yellow,red
# card value=> 1,2,3,4,5,6,7,8,9,10

class Card2:
    def __init__(self,type,value):
        self.type=type
        self.value=value

    def __repr__(self):
        return f"{self.type}{self.value}"

class Allcards:
    def __init__(self):
        type=["green","blue","yellow","red"]
        value=["1","2","3","4","5","6","7","8","9","10"]
        self.cards=[Card2(type,value) for type in types for value in values]
        #for type in types:
        #    for value in values:
        #        self.cards.append(Card2(type,value))
        print(self.cards)

Allcards()



