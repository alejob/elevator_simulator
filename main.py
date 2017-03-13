from elevator_sim import Building, Elevator, Person, Brain

import numpy as np

#initialize building
building = Building(10, 20, 4)


#print building.create_elevators()

"""
print building.floors
print building.array_elevators[0]
print building.array_elevators[0].capacity
print building.set_elevators(20, 2, 4)
print building.array_elevators[0]
print "piso ascensor", building.array_elevators[0].current_floor
print building.array_elevators
print len(building.array_inhabitants)
print building.array_inhabitants[134].current_floor

print "piso ascensor", building.array_elevators[0].current_floor
print building.array_elevators[0].move("down")
print "piso ascensor", building.array_elevators[0].current_floor

print "ESTADO FINAL"
print "ascensor A, piso: ", building.array_elevators[0].current_floor
print "ascensor B, piso: ", building.array_elevators[1].current_floor

#print building.array_inhabitants[134].call_elevator("down",building.array_elevators)


print "ascensor A, calling: ", building.array_elevators[0].calling_floor
print "ascensor B, calling: ", building.array_elevators[1].calling_floor

#building_brain = Brain(building)
"""
#print building.array_inhabitants[134].call_elevator("down", building_brain)
#print building.array_inhabitants[134].call_elevator("down")
#print building.brain
#print building.array_inhabitants[134].set_elevator(0)


for i in range(100):
    select_inhab = np.random.randint(len(building.array_inhabitants))
    print select_inhab
    #go home
    if building.array_inhabitants[select_inhab].current_floor == 0:
        building.array_inhabitants[select_inhab].call_elevator("up")
        living_floor = building.array_inhabitants[select_inhab].living_floor
        building.array_inhabitants[select_inhab].set_elevator(living_floor)
        building.array_inhabitants[select_inhab].current_floor = living_floor
    #go to work
    else:
        building.array_inhabitants[select_inhab].call_elevator("down")
        building.array_inhabitants[select_inhab].set_elevator(0)
        building.array_inhabitants[select_inhab].current_floor = 0
        
    print "total time ", building.brain.arrived() - building.brain.time_start
    print "current floor", building.array_inhabitants[select_inhab].current_floor


print "yyy"
building.array_elevators[0].current_floor = 2
print "changed floor: ", building.array_elevators[0].current_floor
print "brain-piso: ", building.brain.get_elevators_current_floor()
print "brain-destination: ", building.brain.destination
print "brain-calling: ", building.brain.calling
building.brain.move_elevators()
print "changed floor elevator 2: ", building.array_elevators[1].current_floor

