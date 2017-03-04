from elevator_sim import Building, Elevator, Person

#initialize building
building = Building(10, 20, 2)


#print building.create_elevators()

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

print building.array_inhabitants[134].call_elevator("down",building.array_elevators)

print "ascensor A, calling: ", building.array_elevators[0].calling_floor
print "ascensor B, calling: ", building.array_elevators[1].calling_floor
