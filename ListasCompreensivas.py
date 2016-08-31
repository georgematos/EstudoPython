# uma lista dos numeros de 1 a 20 dobrados divisíveis pro 3
doubles_by_three = [x * 2 for x in range(1, 20) if (x * 2) % 3 == 0]
# uma lista dos numeros pares de 1 a 11 elevados a 2
even_squares = [x ** 2 for x in range(1, 11) if (x ** 2) % 2 == 0]

cubes_for_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]

print(doubles_by_three)
print(even_squares)
print(cubes_for_four)

# Lista compreensiva com condição
# Cria uma lista dos numeros entre 1 e 15 divisíveis por 3 e 5
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)