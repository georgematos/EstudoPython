#Fitra a lista para remover os numeros impares
def purify(numeros):
	pares = []
	for i in range(len(numeros)):
		if numeros[i] % 2 == 0:
			pares.append(numeros[i])
	return pares

numeros = [4,5,5,4]
print(purify(numeros))
