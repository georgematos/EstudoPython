def factorial(x):
	if x <= 0:
		return 0
	elif x == 1:
		return 1
	else:
		fatorial = 1
		for i in range(1, x+1):
			fatorial *= i
		return fatorial

n = int(input("Digite um numero: "))

print(factorial(n))