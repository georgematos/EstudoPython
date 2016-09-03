# Conversao de numero binário para decimal na mão:
# 8 4 2 1 (Sequencia binária, potências de 2.)
# 1 0 1 0 (1 é como se o bit fosse ligado.)
# 8+0+2+0 = 10

print(0b1)   #1
print(0b10)  #2
print(0b11)  #3
print(0b100) #4
print(0b101) #5
print(0b110) #6
print(0b111)   #7
print("******")
print(0b1 + 0b11)  #4
print(0b11 * 0b11) #9

#256 128 64 32 16 8 4 2 1

um = 0b1
dois = 0b10
tres = 0b11
quatro = 0b100
cinco = 0b101
seis = 0b110
sete = 0b111
oito = 0b1000
nove = 0b1001
dez = 0b1010
onze = 0b1011
doze = 0b1100

# A função bin() recebe um numero inteiro e retorna sua reprenstação 
# binaria em forma de string 
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))
print("*******")

# A função int() pode receber um numero e a base em que ele está e
# convertê-lo para a base 10:
print(int("110", 2)) # retornará 6
print("*******")

# Deslocamento de bits
shift_right = 0b1100
shift_left = 0b1

print(shift_right, bin(shift_right))
print(shift_left, bin(shift_left))

shift_right = shift_right >> 2 # 3
shift_left = shift_left << 2 # 4

print(shift_right, bin(shift_right))
print(shift_left, bin(shift_left))
print("*******")

# Operadores lógicos

# & compara os dois numeros binários e retorna outro onde as posições
# dos 1's sejam iguais em ambos
print(bin(0b1110 & 0b101)) # 0b100
# | compara os dois numeros binários e retorna outro onde as posições
# terão 1 onde qualquer um dos dois numeros comparados tenha 1
print(bin(0b1110 | 0b101)) # 0b1111
# ^ retorna 1 onde apenas um dos dois números tenha 1
print(bin(0b1110 ^ 0b101)) # 0b1011
# ~ equivale a somar 1 ao número e torná-lo negativo
print(0b1011) # 11
print(~0b1011) # -12 -0b1100

# Usando mascara para verificar se um bit está ativo:
def check_bit4(input):
    mask = 0b1000 # para verificar se o 4º bit está ativo
    desired = input & mask
    if desired > 0:
        return "ativo"
    else:
        return "inativo"

# Usando mascara para ativar um bit:
a = 0b10111011
mask = 0b0100 # ativa o terceiro bit
desired = a | mask
print(bin(desired))

# Usando mascara para ativar um bit:
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(bin(desired))

# Usado deslocamento de bits para criar máscaras
def flip_bit(number, n): #0b00111, 2
	mask = 0b1 << n-1
	result = number ^ mask
	return bin(result)