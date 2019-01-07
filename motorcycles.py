motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles_orig = motorcycles.copy()

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = motorcycles_orig.copy()

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

print (motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print (motorcycles)

motorcycles.insert(0, 'ducati')
print (motorcycles)

motorcycles = motorcycles_orig.copy()

print (motorcycles)
del motorcycles[0]
print (motorcycles)

motorcycles = motorcycles_orig.copy()

del motorcycles[1]
print(motorcycles)

motorcycles = motorcycles_orig.copy()

print (motorcycles)

popped_motorcycle = motorcycles.pop()
print (motorcycles)
print (popped_motorcycle)

motorcycles = motorcycles_orig.copy()

last_owned = motorcycles.pop()

print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = motorcycles_orig.copy()
motorcycles.append('ducati')
print (motorcycles)

motorcycles.remove('ducati')
print (motorcycles)

motorcycles = motorcycles_orig.copy()
motorcycles.append('ducati')

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

motorcycles.append("suzuki")
print (motorcycles)
motorcycles = [i for i in motorcycles if i != 'suzuki']
print (motorcycles)