# Using __init__ method and self keyword in python
class Car:
        def __init__(self, speed, color,price,fuel):
                self.speed=speed
                self.color = color
                self.price= price
                self.fuel =fuel

ford = Car(200,'red',1000000,"Electric")
honda = Car(250,'blue',800000,"Diesel")
audi = Car(300,'black',900000,"Gas")
tata =Car(150,"silver",700000,"petrol")

print("Color of tata is",tata.color)
print("Speed of tata is",tata.speed)
print("Price of tata is",tata.price)
print("Fuel of tata is",tata.fuel)

print("Color of ford is",ford.color)
print("Speed of ford is",ford.speed)
print("Price of ford is",ford.price)
print("Fuel of ford is",ford.fuel)

print("Color of honda is",honda.color)
print("Speed of honda is",honda.speed)
print("Price of honda is",honda.price)
print("Fuel of honda is",honda.fuel)