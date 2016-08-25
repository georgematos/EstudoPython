""" Existem 3 formas de remover um item de uma lista,
cada uma com sua peculiaridade """

# Primeira forma: pop()
""" A função pop de uma lista remove o item no indice
indicado e retorna o valor da posição """

n = [1, 3, 5]

removido = n.pop(1)
print(n)
print(removido)

# Segunda forma: remove()
""" A função remove de uma lista irá remover o valor
passado para ela se encontrado, sem necessidade de 
passar o índice e sem retorar o valor """

n = [1, 3, 5]

n.remove(3)

print(n)

# Terceira forma: del()
""" A função nativa do Python del() remove o item no
indice passado, assim como pop() mas não retorna
o valor """

n = [1, 3, 5]

del(n[1])

print(n)

#### testes

board = []
for i in range(0, 5):
    board.append(["O"] * 5)
for i in range(0, len(board)):
    print(" ".join(board[i]))