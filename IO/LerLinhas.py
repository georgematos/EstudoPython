file = open("output.txt", "r")

# print(file.readline())
# print(file.readline())
# print(file.readline())

n_line = 1
for linha in file:
	print("%d elev. a 2 é %s" % (n_line, linha))
	n_line += 1

file.close()