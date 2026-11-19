def llegar_a_1(n):
    if n > 1:
        n -= 1
        llegar_a_1(n)
        print(n)
    else:
        print("Felicidades llegaste a 1")


# llegar_a_1(5)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"EL factorial de 5 es: {factorial(5)}")