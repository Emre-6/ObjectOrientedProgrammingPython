class Pet:
    pets=["Cat","Dog","Bird"]
    
    def __init__(self,name,type):
        
        if type not in Pet.pets: 
            raise ValueError(f"{type} is not a pet.")
        self.name=name
        self.type=type

    def set_type(self,type):
        if type not in Pet.types:
            raise ValueError(f"{type} is not a pet.")
        self.type=type
        
cotton=Pet("Cotton","Cat")
Pasa=Pet("Pasa","Dog")
orange=Pet("Orange","Bird")

cotton.pets.append("Fish")

print(Pet.pets)
print(cotton.pets)
print(Pasa.pets)
print(orange.pets)

