my_list = list(range(16))

without_lambda = []
for x in my_list:
	if x % 3 == 0:
		without_lambda.append(x)
print(without_lambda)

with_lambda = list(filter(lambda x: x % 3 == 0, my_list))
print(with_lambda)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))

# cria uma lista com os numeros de 1 a 10 elevados ao quadrado
squares = [x ** 2 for x in range(1,11)]
print(squares)
# filtra a lista para exibir os numeros maiores que 30 e menores que 70 (inclusive)
print(list(filter(lambda x: x >= 30 and x <= 70, squares)))

