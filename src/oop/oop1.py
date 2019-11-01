# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    """
    Base/Parent class
    """
    # def __init__(self, name):
    #     self.name = name
    pass

class FlightVehicle(Vehicle):
    """
    Sub class for Vehicle
    """
    pass

class GroundVehicle(Vehicle):
    """
    Sub class for Vehicle
    """
    pass

class Starship(FlightVehicle):
    """
    Sub class for FlightVehicle
    """
    pass

class Airplane(FlightVehicle):
    """
    Sub class for FlightVehicle
    """
    pass

class Car(GroundVehicle):
    """
    Sub class for GroundVehicle
    """
    pass

class Motorcycle(GroundVehicle):
    """
    Sub class for GroundVehicle
    """
    pass
