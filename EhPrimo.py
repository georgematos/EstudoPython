def is_prime(x):
    isprime = False
    if x < 2:
        isprime = False
    elif x == 2 or x == 3:
        isprime = True
    else:
        for n in range(2, x):
            if x % n == 0:
                isprime = False
                break
            else:
                isprime = True

    return isprime

num = int(input("Insira o numero: "))
print(is_prime(num))