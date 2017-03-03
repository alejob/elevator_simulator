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
        
    def set_elevators(self,capacity = 10, velocity = 1, current_floor = 1):
        """
        Define custom elevators
        """
        self.array_elevators = []
        for elevator in range(self.elevators):            
            self.array_elevators.append(Elevator(capacity, velocity, current_floor))
    
    def call_elevator(self, call_floor):
        


class Elevator:
    def __init__(self, capacity = 10, velocity = 1, current_floor = 1):
        self.capacity = capacity
        self.velocity = velocity
        self.current_floor = current_floor
"""    
    def move(direction):
        if direction == up:
            up
        elif direction == down:
            down
        else:
            stop

    def sensor(call, current_floor, position_others_elevators):
        #maybe this should be learned automatically
        if call > current_floor:
            go up
        elif call < current_floor:
            go down
        elif call == current_floor:
            keep on floor
        #black box and ...
        return(direction)
        

class Person:
    def __init__(self, time_leave, time_arrive, living_floor):
        self.time_leave = time_leave
        self.time_arrive = time_arrive
        self.living_floor = living_floor
"""
