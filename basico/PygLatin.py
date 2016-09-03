# Tradutor de PygLatin

word = raw_input("Digite a palavra: ")
if type(word) is str and len(word) > 0:
    pyg = "ay"
    firstLetter = word[0]
    otherLetters = word[1:]
    pyglatin = otherLetters + firstLetter + pyg
    pyglatin = pyglatin.lower()

    print(pyglatin)
else:
  print("Por favor digite uma palavra antes de continuar...")

