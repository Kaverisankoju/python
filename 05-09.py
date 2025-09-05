class Vechicle:
    comapany_name = 'BMW' 

    def __init__(self, color, brand, model, fuel_type):
        self.color = color
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def display(self):
        print("color of vechicle", self.color)
        print("brand of vechile", self.brand)
        print("model of vechicle", self.model)
        print("fuel_type", self.fuel_type)

    @classmethod
    def company_name(cls):
        print("company name:", cls.comapany_name)

    @staticmethod
    def vechicle_category():
        print("vechicle are used for trasport")


print("\n----Single Inheritance-----")
class Car(Vechicle):
    def __init__(self, color, brand, model, fuel_type, seats):
        super().__init__(color, brand, model, fuel_type)
        self.seats = seats

    def display(self):
        super().display()
        print("seats in car:", self.seats)


print("\n---Multiple Inheritance---")
class Electric:
    @staticmethod
    def electric_info():
        print("This vehicle uses an electric battery.")

class ElectricCar(Car, Electric):
    def __init__(self, color, brand, model, seats, battery_capacity):
        Car.__init__(self, color, brand, model, "Electric", seats)
        self.battery_capacity = battery_capacity

    def display(self):
        super().display()   
        print(f"Battery Capacity:{self.battery_capacity} kwh")


print("\n---Multi-Level Inheritance---")
class SportsCar(Car):
    def __init__(self, color, brand, model, fuel_type, seats, Max_speed):
        super().__init__(color, brand, model, fuel_type, seats)
        self.max_speed = Max_speed

    def display(self):
        super().display()
        print(f"Max speed of SportsCar {self.max_speed} km/h")


print("\n---Hierachical Inheritance---")
class Bike(Vechicle):
    def __init__(self, color, brand, model, fuel_type, engine_cc):
        super().__init__(color, brand, model, fuel_type)
        self.engine_cc = engine_cc

    def display(self):
        super().display()
        print(f"Engine:{self.engine_cc}cc")

class bus(Vechicle):
    def __init__(self, color, brand, model, fuel_type, no_of_people):
        super().__init__(color, brand, model, fuel_type)
        self.no_of_people = no_of_people

    def display(self):
        super().display()
        print(f"number of people in bus:{self.no_of_people}")


print("\n---Hybrid Inheritance---")
class HybridCar(ElectricCar, SportsCar):
    def __init__(self, color, brand, model, seats, battery_capacity, Max_speed):
        ElectricCar.__init__(self, color, brand, model, seats, battery_capacity)
        self.max_speed = Max_speed

    def display(self):
        super().display()  
        print(f"Max speed of HybridCar {self.max_speed} km/h")
        print("This is a Hybrid Car with both Electric & Fuel engine.")


print("\n---Creating Vechicles---")
v1 = Vechicle("black", "Tata", "Truck", "Diesel")
v2 = Car('blue', 'Toyota', 'Innova', 'petrol', 6)
v3 = ElectricCar('violet', 'Tesla', 'Model S', 5, 100)
v4 = SportsCar('red', 'Ferrari', '488', 'petrol', 2, 340)
v5 = Bike('white', "Yamaha", "R15", "Petrol", 155)
v6 = bus('yellow', 'Tata', 'City Bus', 'diesel', 80)
v7 = HybridCar('ash', 'BMW', 'i8', 4, 50, 250)

print("\n---display info---")
v2.display(); print("---")
v3.display(); print("---")
v4.display(); print("---")
v5.display(); print("---")
v6.display(); print("---")
v7.display()

print("\n---Class method---")
Vechicle.company_name()

print("\n---static method---")
Vechicle.vechicle_category()
Electric.electric_info()
