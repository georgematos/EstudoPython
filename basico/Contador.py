def count(sequence, item):
	contador = 0
	sequencia = sequence.split(",")
	for i in sequencia:
		if i == item:
			contador += 1
	return contador

sequence = input("Digite uma sequencia de" +
 " palavras separadas por virgula: ")
item = input("Digite uma palavra para conta-la: ")

print(count(sequence, item))

''' Exercicio da Codecademy
def count(sequence, item):
	contador = 0
	
	for i in sequence:
		if i == item:
			contador += 1
	return contador
'''