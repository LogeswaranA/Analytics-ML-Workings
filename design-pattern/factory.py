from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        return "Driving a sedan..."

class SUV(Car):
    def drive(self):
        return "Driving an SUV..."

class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError(f"Unknown car type: {car_type}")

# Usage
car1 = CarFactory.create_car("sedan")
car2 = CarFactory.create_car("suv")

print(car1.drive())  # Output: Driving a sedan...
print(car2.drive())  # Output: Driving an SUV...
