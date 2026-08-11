# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview
This assignment explored object-oriented programming concepts in Python, focusing on inheritance, namespaces, and object copying.

## Implementation Summary
I created a `Vehicle` parent class that tracks a shared vehicle count and stores make, model, year, and a mutable features list. The `ElectricVehicle` child class inherits from `Vehicle`, adds battery capacity, range, and charge level, introduces a new `power_source` class variable, provides a `charge()` method, and overrides the `info()` method to include electric-specific details.

Namespace behavior was demonstrated by creating two `ElectricVehicle` instances, accessing class variables both through the class and through instances, dynamically adding an `owner` attribute to only one instance, and printing both instance `__dict__` and selected class namespace entries.

Shallow and deep copying were shown using an `ElectricVehicle` that contains a nested mutable features list. After modifying the original object’s list and charge level, the shallow copy reflected the list change (shared reference) while the deep copy remained independent.

An extension was added: a class method `total_vehicles()` on `Vehicle` and an instance method `remaining_range()` on `ElectricVehicle` that estimates driving range from the current charge percentage.