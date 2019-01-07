cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_original = cars.copy()
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars=cars_original.copy()

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print("\nThis is the length of the list:")
print(str(len(cars)) + "\n")

cars = sorted(cars_original.copy())

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
