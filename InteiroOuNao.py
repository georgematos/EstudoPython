import math

def is_int(x):
    if x < 0:
        x_round = math.trunc(x)
    else:
        x_round = math.floor(x)

    if x_round == x:
        return True
    else:
        return False

numero = float(input("Digite um numero: "))

if is_int(numero):
	print("O Numero é inteiro.")
else:
	print("O Numero não é inteiro.")