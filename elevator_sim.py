import numpy as np
import time

array_elevators = [1,2,3]

class Building:
    def __init__(self, floors, inhabitants_per_floor, elevators):
        #floors doesn't include level 0, ex: floor = 10, mean 10 floor + level 0
        self.floors = floors
        self.inhabitants_per_floor = inhabitants_per_floor
        self.elevators = elevators
        self.total_inhabitants = inhabitants_per_floor * floors
        #Create a building with a brain
        self.brain = Brain()
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
                #with the last "self" I call Building Class and set to the inhabitant
                self.array_inhabitants.append(Person(800, 1700, current_floor+1, 0, living_floor+1, self))
        

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
    

class Person:
    def __init__(self, time_leave, time_arrive, current_floor, destination_floor, living_floor, current_building):
        self.time_leave = time_leave
        self.time_arrive = time_arrive
        self.current_floor = current_floor
        self.destination_floor = destination_floor
        self.living_floor = living_floor
        self.building = current_building
        
    def call_elevator(self, direction):
        current_floor = self.current_floor #calling floor is the current floor
        calling_floor = current_floor
        self.building.brain.calling_elevator(calling_floor, direction)
        
    #destiny floor
    def set_elevator(self, destination_floor):
        self.building.brain.destination_floor(destination_floor)


class Brain:
    def __init__(self):
        #self.buildingg = buildingg
        self.time_start = time.time() 
        self.time_end = None
   
    def calling_elevator(self, calling_floor, direction):
        print "Brain: orden recibida, llamado desde el piso", calling_floor
        elevators_current_floor = self.get_elevators_current_floor()
        return 0
    
    def destination_floor(self, destination_floor):
        print "Brain: orden recibida, ir al piso", destination_floor
        return 0
    
    def arrived(self):
        self.time_end = time.time()
        return self.time_end
        
    def get_elevators_current_floor(self):
        for i in range(len(array_elevators)):
            #building.array_elevators[i].current_floor
            print "hola"
