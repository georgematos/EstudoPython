def is_prime(x):
    isprime = True
    if x < 2:
        isprime = False
    else:
        for n in range(2, x):
            if x % n == 0:
                isprime = False
                break

    return isprime

num = int(input("Insira o numero: "))
print(is_prime(num))
