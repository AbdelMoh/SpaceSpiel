class Car :

    def __init__(self,car_brand,color,horse_power):
        self.car_brand =car_brand
        self.color = color
        self.horse_power = horse_power
        self.positionX = 5
        self.positionY = 5

    # def __init__(self):
    #     self.car_brand = None
    #     self.color = None
    #     self.horse_power = None
    #     self.positionX = 5
    #     self.positionY = 5

    def drive (self,x,y):
        self.positionX = x
        self.positionY = y
    def print_position (self):
        print (f"Das aktuelle Auto ist {self.car_brand} in PositionX {self.positionX} und  in PositionY {self.positionY}")

# car1 = Car()
# car1.car_brand = "Audi"
# car1.color = "black"
# car1.horse_power = "400 horse_power"

car2 = Car("BMW","weiß","730")
car2.drive(7,9)
car2.print_position()

# print(car1.car_brand  + " have " + car1.color + " and " + car1.horse_power )
# car1.drive(6,10)
# car1.print_position()
