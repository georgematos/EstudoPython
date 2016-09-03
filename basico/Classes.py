class Animal:
	is_alive = True
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return "(Nome: %s, Idade: %d)" % (self.name, self.age)

	def send_roar(self):
		print("Animal emitindo som ROOOOAAARRR")

hippo = Animal("Smough", 30)
cat = Animal("Meg", 0.4)

print(hippo.is_alive)
print(cat.is_alive)

hippo.is_alive = False

print(hippo.is_alive)
print(cat.is_alive)

print(hippo.__repr__())
hippo.send_roar()
