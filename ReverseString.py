def reverse(text):
	reversed = []
	position_inverted = len(text)-1
	for i in range(0, len(text)):
		reversed.append(text[position_inverted])
		position_inverted -= 1
	return ''.join(reversed)

word = input("Digite uma palavra: ")

print(reverse(word))