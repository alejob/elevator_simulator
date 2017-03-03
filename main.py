from elevator_sim import Building#, Elevator, Person

#initialize building
building = Building(10, 20, 2)


#print building.create_elevators()

print building.floors
print building.array_elevators[0]
print building.array_elevators[0].capacity
print building.set_elevators(20, 2, 4)
print building.array_elevators[0]
print building.array_elevators[0].current_floor
print building.array_elevators
