import numpy as np


class Building:
    def __init__(self, floors, inhabitants_per_floor, elevators):
        self.floors = floors
        self.inhabitants_per_floor = inhabitants_per_floor
        self.elevators = elevators
        self.total_inhabitants = inhabitants_per_floor * floors
        #init defaults elevators
        self.array_elevators = []
        for elevator in range(self.elevators):
            self.array_elevators.append(Elevator())
        #init people in all the building
        self.array_inhabitants = []
        for current_floor in range(self.floors):
            #self.array_inhabitants[]
            living_floor = current_floor # init where person lives
            for inhabitant in range(self.inhabitants_per_floor):
                self.array_inhabitants.append(Person(800, 1700, current_floor, 0, living_floor))
        

    def set_elevators(self,capacity = 10, velocity = 1, current_floor = 1):
        """
        Define custom elevators
        """
        self.array_elevators = []
        for elevator in range(self.elevators):            
            self.array_elevators.append(Elevator(capacity, velocity, current_floor))
    
    

class Elevator:
    def __init__(self, capacity = 10, velocity = 1, current_floor = 1):
        self.capacity = capacity
        self.velocity = velocity
        self.current_floor = current_floor
        self.calling_floor = None
    
    def move(self, direction):
        if direction == "up":
            self.current_floor += 1
        elif direction == "down":
            self.current_floor -= 1
        else:
            return 0

    #def sensor(calling_floor, current_floor = self.current_floor,position_others_elevators):
    #def sensor(self, calling_floor, current_floor = 0):
    def sensor(self, calling_floor):
        #current_floor = self.current_floor
        self.calling_floor = calling_floor
        #maybe this should be learned automatically
        """
        if call > current_floor:
            go up
        elif call < current_floor:
            go down
        elif call == current_floor:
            keep on floor
        #black box and ...
        
        return(direction)
        """
        return calling_floor

class Person:
    def __init__(self, time_leave, time_arrive, current_floor, destination_floor, living_floor):
        self.time_leave = time_leave
        self.time_arrive = time_arrive
        self.current_floor = current_floor
        self.destination_floor = destination_floor
        self.living_floor = living_floor

    def call_elevator(self, direction, array_elevators):
        current_floor = self.current_floor #piso de llamada es el actual
        calling_floor = current_floor
        for elevator in array_elevators:
            elevator.sensor(calling_floor)
        return direction
