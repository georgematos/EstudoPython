# Gera uma lista com os quadrados dos números de 1 a 10
my_list = [i**2 for i in range(1,11)]

file = open("output.txt", "w")

for item in my_list:
	file.write(str(item) + "\n")

file.close()