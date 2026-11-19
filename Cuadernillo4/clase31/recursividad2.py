# def sumar(n):
#     suma_total = 0
#     for i in range(n):
#         suma_total += (i+1)
#     return suma_total

# print(f"La suma es de: {sumar(5)}")

def sumar(n):
    if n > 0:
        return n + sumar(n-1)
    else:
        return 0


print(f"La suma es de: {sumar(5)}")