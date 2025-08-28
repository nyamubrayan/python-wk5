# Base class (optional)
class Vehicle:
    def move(self):
        pass  # placeholder for polymorphism


# Different vehicle classes with the same method name `move`
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ")

class Bike(Vehicle):
    def move(self):
        print("Riding on the path ")


# Polymorphism in action
def main():
    vehicles = [Car(), Plane(), Boat(), Bike()]

    print("=== Vehicle Movements ===")
    for vehicle in vehicles:
        vehicle.move()  # same method, different behavior

if __name__ == "__main__":
    main()
