class Computer:
    def __init__(self):
        self.__maxprice = 900
        self.name = "Dell"
    def  sell(self):
        print("Model: ",self.name)
        print("Selling Price: ", self.__maxprice)
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()    
c.sell()    
c.name = "Hp"
c.__maxprice = 1000
c.sell()
      