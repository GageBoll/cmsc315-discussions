"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================
INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.
class Vehicle:
    # Class variable shared by all vehicles
    vehicle_count = 0

    def __init__(self, make, model, year):
        self.make = make          # instance variable
        self.model = model        # instance variable
        self.year = year          # extra useful instance data
        self.features = []        # nested mutable list (used later for copying demo)
        Vehicle.vehicle_count += 1

    def info(self):
        """Return a string describing the vehicle."""
        return f"{self.year} {self.make} {self.model}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.
class ElectricVehicle(Vehicle):
    # New class variable
    power_source = "electric"

    def __init__(self, make, model, year, battery_kwh, range_miles):
        # Call parent constructor
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh      # new instance variable
        self.range_miles = range_miles      # new instance variable
        self.charge_level = 100             # extra state

    def charge(self, amount=10):
        """New method: increase charge level (capped at 100)."""
        self.charge_level = min(100, self.charge_level + amount)
        return f"Charged to {self.charge_level}%"

    def info(self):
        """Override parent info() to include electric-specific details."""
        base = super().info()
        return f"{base} | {self.battery_kwh} kWh battery | {self.range_miles} mi range | Charge: {self.charge_level}%"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two ElectricVehicle objects
    ev1 = ElectricVehicle("Tesla", "Model 3", 2024, 75, 272)
    ev2 = ElectricVehicle("Nissan", "Leaf", 2023, 40, 149)

    # Access class variable through the class
    print(f"Class variable via class: ElectricVehicle.power_source = {ElectricVehicle.power_source}")
    print(f"Class variable via class: Vehicle.vehicle_count = {Vehicle.vehicle_count}")

    # Access the same class variable through an object
    print(f"Class variable via object (ev1): {ev1.power_source}")
    print(f"Class variable via object (ev2): {ev2.power_source}")

    # Add a new attribute to only one object after creation
    ev1.owner = "Alex Rivera"          # this exists only on ev1

    # Display each object's namespace
    print("\nev1.__dict__ (instance namespace):")
    print(ev1.__dict__)
    print("\nev2.__dict__ (instance namespace):")
    print(ev2.__dict__)

    # Display information about the class namespace
    print("\nElectricVehicle.__dict__ (class namespace - selected keys):")
    for key in ["power_source", "charge", "info", "__init__"]:
        print(f"  {key}: {ElectricVehicle.__dict__.get(key)}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object that contains nested mutable data (the features list)
    original = ElectricVehicle("Ford", "Mustang Mach-E", 2025, 91, 300)
    original.features.append("Autopilot")
    original.features.append("Heated Seats")
    original.owner = "Jordan Lee"

    # Create a shallow copy
    # Shallow copy: new object, but nested mutable objects (like the features list)
    # are still shared references. Changing the list in one affects the other.
    shallow = copy(original)

    # Create a deep copy
    # Deep copy: completely independent object; nested mutables are also copied.
    # Changes to the original's nested data do NOT affect the deep copy.
    deep = deepcopy(original)

    # Modify the original object's nested data
    original.features.append("Premium Sound")
    original.charge_level = 45          # also change a simple attribute

    # Display results
    print("Original after modification:")
    print(f"  info: {original.info()}")
    print(f"  features: {original.features}")
    print(f"  owner: {getattr(original, 'owner', None)}")

    print("\nShallow copy (shares the features list):")
    print(f"  info: {shallow.info()}")
    print(f"  features: {shallow.features}")   # will show the new item
    print(f"  owner: {getattr(shallow, 'owner', None)}")

    print("\nDeep copy (independent features list):")
    print(f"  info: {deep.info()}")
    print(f"  features: {deep.features}")      # still the original two items
    print(f"  owner: {getattr(deep, 'owner', None)}")


# Student-created extension:
# Added a simple class method that reports how many Vehicle instances exist
# and a convenience method on ElectricVehicle that returns remaining range
# based on current charge level.
@classmethod
def total_vehicles(cls):
    return f"Total vehicles created: {cls.vehicle_count}"

Vehicle.total_vehicles = total_vehicles   # attach the extension

def remaining_range(self):
    """Estimate remaining range based on current charge percentage."""
    return round(self.range_miles * (self.charge_level / 100), 1)

ElectricVehicle.remaining_range = remaining_range


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.
def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    print("\n--- Parent object ---")
    gas_car = Vehicle("Toyota", "Camry", 2022)
    gas_car.features.append("Backup Camera")
    print(gas_car.info())
    print(Vehicle.total_vehicles())          # extension

    # Create and test a child object
    print("\n--- Child object ---")
    my_ev = ElectricVehicle("Hyundai", "Ioniq 5", 2024, 77, 303)
    print(my_ev.info())                      # overridden method
    print(my_ev.charge(15))                  # new method
    print(f"Estimated remaining range: {my_ev.remaining_range()} miles")  # extension
    print(Vehicle.total_vehicles())

    # Demonstrate inheritance
    print("\n--- Inheritance check ---")
    print(f"Is my_ev a Vehicle? {isinstance(my_ev, Vehicle)}")
    print(f"Is my_ev an ElectricVehicle? {isinstance(my_ev, ElectricVehicle)}")

    # Call demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()