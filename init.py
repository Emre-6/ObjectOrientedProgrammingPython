class Product:
    def __init__(self, _name, price, isActive=False):
        self.name=_name
        self.price=price
        self.isActive=isActive
        print('Products')

p1=Product("Samsung S10",5000, True)
p2=Product("IPhone 12",8000, False)

print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)



        

        