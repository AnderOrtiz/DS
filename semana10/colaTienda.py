colaTienda = []

colaTienda.append("Ana")
colaTienda.append("Carlos")
colaTienda.append("Luis")

print(f"Cliente de la Tienda Rosita: {colaTienda}")

# Operación Peek
print(f"Siguiente cliente: {colaTienda[0]}")

# Operación SIZE
# Consilta cianto clientes hay
print(f"Clientes en espera: {len(colaTienda)}")

#Atender el primer cliente
cliente = colaTienda.pop(0)
print(f"Cliente atendido: {cliente}")

#Mostrar los clientes que siguen:
print(f"Locs clientes de la cola son: {colaTienda}")

print(f"El ultimo cliente: {colaTienda[-1]}")

#operación IS EMPTY
#conpueba si todavia hay elementos(Clientes)

cliente = colaTienda.pop(0)
cliente = colaTienda.pop(0)

if not colaTienda:
    print("No hay clientes esperando...")
else:
    print("Todavia hay clientes esperando...")