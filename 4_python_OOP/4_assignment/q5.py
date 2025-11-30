# Concept: Inheritance
''' Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes - seats (in Car) &
engine_cc (in Bike). '''

class Vehical:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return 0
    

class Car(Vehical):
    def __init__(self, brand, model, seat):
        super().__init__(brand, model)
        self.seat = seat
    
    def get_info(self):
        print(f"brand: {self.brand} model: {self.model} capacity: {self.seat}seats")

class Bike(Vehical):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
    
    def get_info(self):
        print(f"Brand: {self.brand} Model: {self.model} engine_power: {self.engine_cc}")

car1 = Car("ferrari","812Superfast", 2)
car2 = Car("toyota", "fortuner", 4)
bike1 = Bike("kawasaki", "ZX-10R", "998cc")

car1.get_info()
bike1.get_info()