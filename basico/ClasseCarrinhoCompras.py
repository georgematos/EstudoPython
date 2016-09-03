class ShoppingCart:
	items_in_cart = {}
	def __init__(self, customer_name):
		self.customer_name = customer_name

	def add_item(self, product, price):
		if not product in self.items_in_cart:
			self.items_in_cart[product] = price
			print(product + " added.")
		else:
			print(product + " already in cart.")

	def remove_item(self, product):
		if product in self.items_in_cart:
			del(self.items_in_cart[product])
			print(product + " removed.")
		else:
			print(product + " there's not in cart")

	def show_items(self):
		for key in self.items_in_cart:
			print("Produto: %s\n  Preço: %d" % (key, self.items_in_cart[key]))

	def get_total(self):
		total = 0
		for key in self.items_in_cart:
			total += self.items_in_cart[key]
		return total

my_cart = ShoppingCart("georgemattos@gmail.com")
print(my_cart.customer_name)

my_cart.add_item("XRE 190", 13000)
my_cart.add_item("Novo Gol", 45000)
my_cart.add_item("Apartamento", 130000)

my_cart.remove_item("Novo Gol")

my_cart.show_items()
print("Total: R$ %.2f" % my_cart.get_total())
