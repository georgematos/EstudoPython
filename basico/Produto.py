def product(inteiros):
	resultado = 1
	for n in inteiros:
		resultado *= n
	return resultado

print(product([4,5,5]))