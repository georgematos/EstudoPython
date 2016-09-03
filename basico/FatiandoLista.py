# Cria uma lista de numeros de 1 a 10
my_list = list(range(1, 11))

# Mostrando os itens ímpares da lista
# my_list[fist:last:strade]
print(my_list[::2])

# Invertendo uma lista
print(my_list[::-1])

""" Exibindo os itens de uma lista de 100 itens
invertidos de 10 em 10 """
to_one_hundred = list(range(101))
print(to_one_hundred[::-10])

# Prova
to_21 = list(range(1,22))
odds = to_21[::2]

# Pra obter o firt: indice
# Pra obter o last: indice+1
middle_third = to_21[7:14:]

print(to_21)
print(odds)
print(middle_third)

string = "ABCDEFJHIJ"
start, end, stride = 1, 6, 2
print(string[start:end:stride])

# Desafio: revelar a mensagem !XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1]
message = message[0::2]
print(message)