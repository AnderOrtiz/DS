def contar_digitos(n):
    n = abs(n)

    if n < 10:
        return 1

    return 1 + contar_digitos(n // 10)


print(f"Dígitos de 1024: {contar_digitos(1024)}")
print(f"Dígitos de 9: {contar_digitos(9)}")