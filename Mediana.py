def media(lista):
	lista_ordenada = sorted(lista)
	tamanho = len(lista_ordenada)
	# Se a lista for par
	if tamanho % 2 == 0:
		media_a = int(tamanho / 2 - 1)
		media_b = int(tamanho / 2)
		return (lista_ordenada[media_a] + lista_ordenada[media_b]) / 2
	# Se a lista for impar
	else: 
		media = int(tamanho / 2)
		return lista_ordenada[media]

print(media([4,5,5,4]))