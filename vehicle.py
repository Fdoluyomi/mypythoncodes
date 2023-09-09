class Vehicle:


    def __init__ (self,name:str,maximumspeed:int,mileage:int):
        self.name=name
        self.maximumspeed=maximumspeed
        self.mileage=mileage




vehicle1=Vehicle("RangeRover",144,14)
vehicle2=Vehicle("Lanborghin",217,8)
vehicle3=Vehicle("Tesla",150,267)


print(vehicle1.name)
print(vehicle2.name)
print(vehicle3.name)



