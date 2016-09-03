def digit_sum(n):
    numero = str(n)
    array_de_numeros = []
    for char in numero:
        array_de_numeros.append(int(char))
    return sum(array_de_numeros)

numero = int(input("Digite um numero: "))

print(digit_sum(numero))