def censor(text, word):
	word_size = len(word)
	if word in text:
		censurado = text.replace(word,"*"*word_size)
	return censurado

texto = input("Digite um texto: ")
palavra = input("Qual palavra de ser censurada: ")
print(censor(texto, palavra))
