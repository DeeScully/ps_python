# assign int to var
cars = 100
# assign float to var
space_in_a_car = 4.
# assign int to var
drivers = 30
# assign int to var
passengers = 90
# eval expression and assign result to var
cars_not_driven = cars - drivers
# 
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
