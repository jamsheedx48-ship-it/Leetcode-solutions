from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def speed(self):
        pass

class Car(Vehicle):
    def start(self):
        print("cart starts")

    def speed(self):
        print("car is high speed")   

class Bike(Vehicle):
    def start(self):
        print("bike starts")

    def speed(self):
        print("bike low speed")    

c=Car()
d=Bike()   


c.speed()
d.start()