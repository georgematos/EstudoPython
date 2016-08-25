def remove_duplicates(lista):
	lista_nova = []
	for item in lista:
		if item not in lista_nova:
			lista_nova.append(item)
	return lista_nova

print( remove_duplicates([1,1,2,2,3,6,4,3,4,7]))