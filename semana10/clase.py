# Sistema de un banco
# Banco los manguitos

cola = []
numero_turno = 1


def registrar_clientes(nombre):
    global numero_turno

    #Generar el codigo de turno
    #T Letra que significa turno
    #:03d minimo de digitos para rellenar son 3
    #Ejemplo: T001

    turno = f"{numero_turno:03d}"
    cliente = [turno, nombre]
    cola.append(cliente)
    numero_turno += 1
    
    #Imprimimos los resultados
    
    print("\nCLiente registrado correctamente.")
    print(f"Turno asignado: {turno}")
    print(f"Cliente: {nombre}")