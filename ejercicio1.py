def potencia(base, exponente):
    if exponente == 0:
        return 1
    
    return base * potencia(base, exponente - 1)


print(f"10 elevado a la 10 es: {potencia(10, 10)}")
print(f"5 elevado a la 4 es: {potencia(5, 4)}")