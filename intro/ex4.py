cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 40

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_capacity_per_car = passengers / cars_driven

print("Total Cars: ", cars)

print("Space in each car: ", space_in_a_car)

print("Total Drivers: ", drivers)

print("Total Passengers: ", passengers)

print("Total cars not driven: ", cars_not_driven)

print("Total Cars Driven: ", cars_driven)

print("Total carpool capacity: ", carpool_capacity)

print("Average Capacity_per_car: ", average_capacity_per_car)
print(id(cars))
cars = 23.45
print(id(cars))
cars = "Ferrari"
print(id(cars))
print("New Cars: ", cars)

drivers = 40

print("Drivers: ", drivers)
print("Cars Driven: ", cars_driven)
