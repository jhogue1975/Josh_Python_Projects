cars = 100						#assigning 100 to variable cars
space_in_a_car = 4.0					# assigning 4 to variable space_in_car
drivers = 30						# assiging 30 to variable drivers
passengers = 90						# assiging 90 to variable passengers
cars_not_driven = cars - drivers			# taking the value in cars and subtracting from drivers and assigning that to cars_not_driven
cars_driven = drivers					# assigning value in drivers to cars_driven
carpool_capacity = cars_driven * space_in_a_car		# multiplying cars_driven by space_in_car and assigning that to carpool_capacity
average_passengers_per_car = passengers / cars_driven	# dividing passengers by cars_driven and assigning that to average_person_per_car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."



i = 4 + 6
x = 5.0 * 40.0 / 3.0
j = 1 + 2 * 3 / 4

k = 1 + x + j


print i
print x
print j
print k