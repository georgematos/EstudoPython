# Não funciona
def anti_vowal(text):
	phrase = list(text)
	for v in phrase:
		if v in "aeiouAEIOU":
			phrase.remove(v)

	return "".join(phrase)

# Funciona
def anti_vowel(text):
	texto_sem_vogal = []
	for v in text:
		if v not in "aeiouAEIOU":
			texto_sem_vogal.append(v)
	return "".join(texto_sem_vogal)

texto = input("Write a text: ")
print(anti_vowal(texto))