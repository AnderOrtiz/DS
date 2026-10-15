from collections import deque
from datetime import datetime


# ============================================================
# DATOS Y ESTRUCTURAS PRINCIPALES
# ============================================================

salidas = [] # creamos una lista vacía que funcionará como pila LIFO para almacenar las salidas de los buses

pasajeros = deque() # creamos una cola de pasajeros utilizando deque(), que permite agregar y eliminar elementos eficientemente desde ambos extremos

siguiente_turno = 1 # declaramos una variable que funcionará como contador para asignar un número de turno a cada pasajero
siguiente_salida = 5001 # declaramos una variable que funcionará como contador para asignar un código único a cada salida registrada


# ============================================================
# ÁRBOL DE DESTINOS
# ============================================================

class NodoDestino:
    # creamos la clase NodoDestino para representar cada nodo del árbol de destinos
    def __init__(self, nombre):
        # inicializamos el nodo y recibimos como parámetro el nombre del destino o región
        self.nombre = nombre # guardamos el nombre recibido como un atributo del objeto
        self.hijos = [] # creamos una lista vacía que almacenará los nodos hijos relacionados con este nodo


# creamos el nodo raíz del árbol, que representa la Terminal Central
raiz = NodoDestino("Terminal Central")

# creamos los nodos que representan las tres regiones principales
zona_oriental = NodoDestino("Zona Oriental")
zona_central = NodoDestino("Zona Central")
zona_occidental = NodoDestino("Zona Occidental")

# agregamos las tres regiones a la lista de hijos del nodo raíz
# extend() permite agregar varios elementos a una lista en una sola operación
# de esta manera, las tres regiones quedan conectadas directamente con la Terminal Central
raiz.hijos.extend([
    zona_oriental,
    zona_central,
    zona_occidental
])

# agregamos los destinos que pertenecen a la Zona Oriental
# cada destino se crea como un objeto NodoDestino y se incorpora a la lista de hijos de esa región
zona_oriental.hijos.extend([
    NodoDestino("San Miguel"),
    NodoDestino("La Unión"),
    NodoDestino("Usulután")
])

# agregamos los destinos que pertenecen a la Zona Central
zona_central.hijos.extend([
    NodoDestino("San Salvador"),
    NodoDestino("La Libertad")
])

# agregamos los destinos que pertenecen a la Zona Occidental
zona_occidental.hijos.extend([
    NodoDestino("Santa Ana"),
    NodoDestino("Ahuachapán")
])


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def solicitar_texto(mensaje):
    # utilizamos un ciclo while True para seguir solicitando información hasta recibir un texto válido
    while True:
        # mostramos el mensaje recibido como parámetro y almacenamos lo que ingrese el usuario
        # strip() elimina los espacios en blanco que se encuentren al principio y al final del texto
        texto = input(mensaje).strip()

        # comprobamos si el texto contiene algún carácter después de eliminar los espacios
        # si no está vacío, devolvemos el texto y finalizamos la función con return
        if texto:
            return texto

        # si el texto está vacío, mostramos un mensaje de error y el ciclo vuelve a solicitar el dato
        print("Error: el dato no puede estar vacío.")


def mostrar_salida(salida):
    # recibimos como parámetro un diccionario que contiene los datos de una salida registrada
    # utilizamos las claves del diccionario para acceder a los valores correspondientes y mostrarlos en pantalla
    print(f"Código de salida: {salida['codigo']}") # mostramos el código asignado a la salida
    print(f"Código del bus: {salida['bus']}") # mostramos el código del bus registrado
    print(f"Destino: {salida['destino']}") # mostramos el destino al que viajará el bus
    print(f"Fecha y hora: {salida['fecha_hora']}") # mostramos la fecha y hora en que se registró la salida


def es_destino_final(nodo):
    # un destino final es un nodo que existe y que no es la terminal ni una de sus regiones
    # las regiones son los hijos directos de la raíz, por eso las descartamos con raiz.hijos
    # centralizamos esta regla aquí para que todas las funciones validen los destinos de la misma forma
    return nodo is not None and nodo is not raiz and nodo not in raiz.hijos


# ============================================================
# PILA LIFO: SALIDAS DE BUSES
# ============================================================

def registrar_salida():
    global siguiente_salida # accedemos a la variable que declaramos fuera de la función

    bus = solicitar_texto("Código del bus: ") # esta función es un input pero con filtros que solucita en termina el código de un bus

# usamos un la función any para devolver true si algún elemento cumple con la condición
#luego hacemos la codición que compara el código del bus con las lista de codigos de buses por salir
# si encuetra uno hace un print con un mensaje y luego un return
    if any(salida["bus"].casefold() == bus.casefold() 
            for salida in salidas):
        print("Error: ya existe una salida registrada con ese código de bus.")
        return

# en caso no encuentre uno solcitamos los demas datos de bus
    destino = solicitar_texto("Destino del bus: ")
    nodo = buscar_destino(raiz, destino)

# si el destino no existe o es la terminal o una región
# imprime un error porque no es un destino final
    if not es_destino_final(nodo):
        print("Error: el destino no existe o no es un destino final.")
        return

# en caso de que no crea una variable llamada salida con los datos del bus
    salida = {
        "codigo": siguiente_salida,
        "bus": bus,
        "destino": nodo.nombre,
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# agrega la salida a la lista de salidas en la cosición de la derecha
    salidas.append(salida)
# aumenta el contador de siguiete_salida
    siguiente_salida += 1

# print de confimarción
    print("\nSalida registrada correctamente.")
# con esta función mostramos los datos de la salida registrada
    mostrar_salida(salida)


def deshacer_salida():
    # validamos si la lista de salidas está vacia
    if not salidas:
        print("No hay salidas registradas para deshacer.")
        return

    # en caso no lo esté, creamos una variable con el ultimo en entrar
    salida = salidas.pop()

    # print de confirmación
    print("\nSe deshizo la última salida registrada:")
    # con esta función mostramos los datos de la salida 
    mostrar_salida(salida)

# esta función imprime todas la salidas
def mostrar_salidas():
# se va a la lista de salidas 
# en caso la lista esté vacia imprime No hay salidas registradas.
    if not salidas:
        print("No hay salidas registradas.")
        return

    print("\n========== SALIDAS REGISTRADAS ==========")

    # en caso la lista de salidas no esté vacia recorre la lista de todas la salidas e imprime sus datos
    for salida in salidas:
        mostrar_salida(salida)
        print("----------------------------------------")

    print(f"Total de salidas registradas: {len(salidas)}")
    print(f"Última salida registrada: {salidas[-1]['codigo']}")


# esta función imprime el último bus en entrar a la lista salidas
def consultar_cima():
# se va a la lista de salidas 
# en caso la lista esté vacia imprime La pila de salidas está vacía.
    if not salidas:
        print("La pila de salidas está vacía.")
        return
# imprime el último bus en entrar a la lista salidas
    print("\n========== ÚLTIMA SALIDA ==========")
    mostrar_salida(salidas[-1])


# ============================================================
# COLA FIFO: ATENCIÓN DE PASAJEROS
# ============================================================

def registrar_pasajero():
    global siguiente_turno # accedemos a la variable que declaramos fuera de la función para poder aumentar el contador de turnos

    # solicitamos el nombre del pasajero utilizando la función que valida que el texto no esté vacío
    nombre = solicitar_texto("Nombre completo del pasajero: ")

    # solicitamos el destino del pasajero
    destino = solicitar_texto("Destino del pasajero: ")

    # buscamos el destino ingresado dentro del árbol de destinos
    nodo = buscar_destino(raiz, destino)

    # comprobamos que el nodo sea un destino final válido
    # si no se encontró, o si corresponde a la terminal central o a una región, no es un destino final
    # en cualquiera de estos casos mostramos un error y salimos de la función con return
    if not es_destino_final(nodo):
        print("Error: el destino no existe o no es un destino final.")
        return

    # creamos un diccionario llamado pasajero con los datos que necesitamos registrar
    pasajero = {
        "turno": f"P{siguiente_turno:03d}", # creamos un turno con una P y un número de tres dígitos, por ejemplo P001
        "nombre": nombre, # guardamos el nombre del pasajero
        "destino": nodo.nombre # guardamos el nombre del destino encontrado en el árbol
    }

    # agregamos el pasajero al final de la cola para respetar el principio FIFO
    # el primero que llega será el primero en ser atendido
    pasajeros.append(pasajero)

    # aumentamos el contador para que el siguiente pasajero reciba un turno diferente
    siguiente_turno += 1

    # mostramos un mensaje de confirmación con el turno asignado al pasajero
    print(f"Pasajero registrado correctamente. Turno: {pasajero['turno']}")


def mostrar_pasajeros():
    # comprobamos si la cola está vacía
    # si no hay pasajeros, mostramos un mensaje y salimos de la función
    if not pasajeros:
        print("No hay pasajeros en espera.")
        return

    # mostramos el encabezado de la sección de pasajeros en espera
    print("\n========== PASAJEROS EN ESPERA ==========")

    # recorremos la cola con un for para obtener los datos de cada pasajero
    for pasajero in pasajeros:
        # mostramos el turno, el nombre y el destino de cada pasajero
        print(
            f"{pasajero['turno']} | "
            f"{pasajero['nombre']} | "
            f"{pasajero['destino']}"
        )

    # utilizamos len() para contar cuántos pasajeros hay actualmente en la cola
    print(f"Total de pasajeros en espera: {len(pasajeros)}")


def atender_pasajero():
    # comprobamos si la cola está vacía antes de intentar retirar un pasajero
    # esto evita errores al utilizar popleft() sin elementos
    if not pasajeros:
        print("No hay pasajeros en espera para atender.")
        return

    # retiramos al primer pasajero de la cola y guardamos sus datos en la variable pasajero
    # popleft() elimina el elemento que se encuentra al principio de la cola
    # esto respeta FIFO: el primero en llegar es el primero en ser atendido
    pasajero = pasajeros.popleft()

    # mostramos el encabezado de la atención
    print("\n========== PASAJERO ATENDIDO ==========")

    # mostramos los datos del pasajero que acaba de ser atendido
    print(f"Turno: {pasajero['turno']}")
    print(f"Nombre: {pasajero['nombre']}")
    print(f"Destino: {pasajero['destino']}")

    # mostramos cuántos pasajeros quedan esperando después de atender al pasajero
    print(f"Total en espera: {len(pasajeros)}")


def consultar_pasajeros_por_destino():
    # solicitamos el destino que queremos consultar
    destino = solicitar_texto("Destino que desea consultar: ")

    # buscamos el destino ingresado dentro del árbol
    nodo = buscar_destino(raiz, destino)

    # si el destino no existe o corresponde a la terminal central o a una región
    # mostramos un mensaje de error y salimos de la función
    if not es_destino_final(nodo):
        print("Error: el destino no existe o no es un destino final.")
        return

    # utilizamos sum() para contar los pasajeros cuyo destino coincide con el consultado
    # la expresión genera un 1 por cada pasajero que cumple la condición y un 0 para los demás
    # casefold() permite comparar los nombres sin distinguir entre mayúsculas y minúsculas
    cantidad = sum(
        1 for pasajero in pasajeros
        if pasajero["destino"].casefold() == nodo.nombre.casefold()
    )

    # mostramos la cantidad de pasajeros que esperan viajar al destino seleccionado
    print(f"Pasajeros esperando hacia {nodo.nombre}: {cantidad}")


# ============================================================
# ÁRBOL: RECORRIDO, BÚSQUEDA Y AGREGAR DESTINOS
# ============================================================

def mostrar_arbol(nodo, nivel=0):
    # mostramos el nombre del nodo actual
    # multiplicamos los espacios por el nivel para representar visualmente la jerarquía
    # el nodo raíz comienza en el nivel 0 y sus hijos se muestran con mayor indentación
    print("    " * nivel + "- " + nodo.nombre)

    # recorremos la lista de hijos del nodo actual
    for hijo in nodo.hijos:
        # llamamos nuevamente a la función para mostrar cada hijo
        # aumentamos el nivel en 1 para indicar que está un nivel más abajo en el árbol
        mostrar_arbol(hijo, nivel + 1)


def buscar_destino(nodo, nombre):
    # comparamos el nombre del nodo actual con el nombre que estamos buscando
    # usamos strip() para eliminar espacios al principio y al final
    # usamos casefold() para comparar los nombres sin distinguir entre mayúsculas y minúsculas
    if nodo.nombre.casefold() == nombre.strip().casefold():
        # si los nombres coinciden, devolvemos el nodo encontrado
        return nodo

    # recorremos todos los hijos del nodo actual para buscar el destino
    for hijo in nodo.hijos:
        # llamamos nuevamente a la función para buscar dentro de cada hijo
        # esto permite explorar también los niveles inferiores del árbol
        resultado = buscar_destino(hijo, nombre)

        # si el resultado no es None, significa que encontramos el destino
        # devolvemos el nodo encontrado sin continuar buscando en los demás hijos
        if resultado is not None:
            return resultado

    # si terminamos de revisar todos los hijos y no encontramos el destino
    # devolvemos None para indicar que no existe en el árbol
    return None


def buscar_destino_menu():
    # solicitamos el nombre del destino que el usuario desea buscar
    nombre = solicitar_texto("Nombre del destino que desea buscar: ")

    # llamamos a buscar_destino() desde la raíz para revisar todo el árbol
    nodo = buscar_destino(raiz, nombre)

    # si el resultado es None, significa que el destino no existe
    if nodo is None:
        print(f"El destino '{nombre}' no existe.")

    # comprobamos si el nodo encontrado es la raíz o una región directamente debajo de ella
    # estos nodos representan la terminal o regiones, no destinos finales
    elif nodo is raiz or nodo in raiz.hijos:
        print("El nombre corresponde a la terminal o a una región, no a un destino final.")

    # si no se cumple ninguna de las condiciones anteriores, encontramos un destino final
    else:
        print(f"Destino encontrado: {nodo.nombre}")


def agregar_destino():
    # solicitamos el nombre de la región donde queremos agregar el nuevo destino
    region = solicitar_texto("Nombre de la región padre: ")

    # buscamos la región ingresada dentro del árbol
    nodo_region = buscar_destino(raiz, region)

    # comprobamos que el nodo sea una de las regiones, es decir, un hijo directo de la raíz
    # no permitimos usar la terminal central como padre, porque el nuevo nodo quedaría como región y no como destino
    # si no existe o no es una región válida, mostramos un error y salimos de la función
    if nodo_region not in raiz.hijos:
        print("Error: la región indicada no existe o no es una región.")
        return

    # solicitamos el nombre del nuevo destino
    nombre = solicitar_texto("Nombre del nuevo destino: ")

    # buscamos el nombre en todo el árbol para evitar duplicar destinos, regiones o la terminal
    if buscar_destino(raiz, nombre) is not None:
        print("Error: ya existe un destino, región o nodo con ese nombre.")
        return

    # creamos un nuevo nodo con el nombre del destino ingresado
    nuevo_destino = NodoDestino(nombre)

    # agregamos el nuevo nodo a la lista de hijos de la región seleccionada
    # de esta manera, el destino queda ubicado en la jerarquía correspondiente
    nodo_region.hijos.append(nuevo_destino)

    # mostramos un mensaje para confirmar que el destino fue agregado correctamente
    print(f"Destino '{nombre}' agregado a '{nodo_region.nombre}'.")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    print("""
            TERMINAL DE BUSES
========================================
PILA LIFO - SALIDAS
1. Registrar salida de bus
2. Deshacer última salida
3. Mostrar salidas registradas
4. Consultar cima de la pila

COLA FIFO - PASAJEROS
5. Registrar pasajero
6. Mostrar pasajeros en espera
7. Atender siguiente pasajero
8. Consultar pasajeros por destino

ÁRBOL DE DESTINOS
9. Mostrar árbol de destinos
10. Buscar destino
11. Agregar destino a una región

0. Salir
========================================
""")


def main():
    # usamos un ciclo while True para mantener el menú funcionando continuamente
    # el ciclo solamente terminará cuando el usuario seleccione la opción de salir
    while True:

        # llamamos a la función que muestra todas las opciones disponibles del sistema
        mostrar_menu()

        # usamos try para intentar convertir la opción ingresada por el usuario a un número entero
        try:
            opcion = int(input("Elija una opción: "))

        # si el usuario ingresa texto u otro valor que no se puede convertir a entero
        # se produce un ValueError y mostramos un mensaje indicando que debe ingresar un número
        except ValueError:
            print("Por favor, ingrese un número válido.")

            # continue hace que el ciclo vuelva al inicio
            # así mostramos nuevamente el menú sin ejecutar ninguna opción
            continue

        # usamos match para evaluar el número ingresado por el usuario
        # cada case representa una opción del menú y ejecuta la función correspondiente
        match opcion:

            case 1:
                # llamamos a la función que registra una nueva salida de bus en la pila
                registrar_salida()

            case 2:
                # llamamos a la función que elimina la última salida registrada
                deshacer_salida()

            case 3:
                # llamamos a la función que muestra todas las salidas registradas
                mostrar_salidas()

            case 4:
                # llamamos a la función que consulta la cima de la pila
                # permite ver la última salida sin eliminarla
                consultar_cima()

            case 5:
                # llamamos a la función que registra un pasajero al final de la cola FIFO
                registrar_pasajero()

            case 6:
                # llamamos a la función que muestra los pasajeros que están esperando
                mostrar_pasajeros()

            case 7:
                # llamamos a la función que atiende al primer pasajero de la cola
                atender_pasajero()

            case 8:
                # llamamos a la función que consulta cuántos pasajeros esperan por un destino específico
                consultar_pasajeros_por_destino()

            case 9:
                # llamamos a la función que muestra el árbol completo de destinos
                # pasamos raiz como argumento para comenzar el recorrido desde el nodo principal
                mostrar_arbol(raiz)

            case 10:
                # llamamos a la función que solicita un destino y busca si existe en el árbol
                buscar_destino_menu()

            case 11:
                # llamamos a la función que agrega un nuevo destino a una región existente
                agregar_destino()

            case 0:
                # mostramos un mensaje de despedida cuando el usuario decide salir
                print("Gracias por utilizar el sistema de la terminal de buses.")

                # break termina el ciclo while y finaliza la ejecución del menú
                break

            case _:
                # el guion bajo (_) funciona como el caso predeterminado
                # se ejecuta cuando el número ingresado no coincide con ninguna opción anterior
                print("Opción no válida. Intente nuevamente.")

        # si la opción no fue salir, solicitamos que el usuario presione Enter antes de continuar
        # esto permite leer los resultados de la operación antes de que aparezca nuevamente el menú
        if opcion != 0:
            input("\nPresione Enter para continuar...")


# esta condición comprueba si el archivo se está ejecutando directamente
# si es así, llama a main() para iniciar el programa
# también permite importar este archivo desde otro módulo sin ejecutar automáticamente el menú
if __name__ == "__main__":
    main()

# ============================================================
# MEJORAS EMPRESARIALES
# ============================================================

# MEJORA 1: CONSULTA DE LA ÚLTIMA SALIDA SIN MODIFICAR LA PILA
# necesidad que resuelve: el personal de la terminal necesita conocer la última salida registrada
# para verificar información o atender consultas, sin correr el riesgo de eliminar un registro válido
# cambio realizado: creamos la función consultar_cima(), que usa salidas[-1] para leer la cima de la pila
# sin retirarla, a diferencia de pop(), que sí la eliminaría

# MEJORA 2: OPTIMIZACIÓN DE LA COLA DE PASAJEROS CON collections.deque
# necesidad que resuelve: los pasajeros deben atenderse en orden de llegada, y con una lista normal
# pop(0) es lento cuando hay muchos pasajeros, porque desplaza todos los elementos restantes (O(n))
# cambio realizado: implementamos la cola con deque(), usando append() para registrar pasajeros al final
# y popleft() para atender al primero, ambas operaciones en O(1) y respetando el orden FIFO
