import builtins
import contextlib
import io

ESTUDIANTES = ["Stanley", "Ortiz", "Ken"]


# A. Cola FIFO de solicitudes
class ColaSolicitudes:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, codigo, cliente):
        # Agrega la solicitud al final de la cola
        self.elementos.append({"codigo": codigo, "cliente": cliente})

    def atender(self):
        # Retira la solicitud más antigua (None si está vacía)
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def existe(self, codigo):
        return any(s["codigo"] == codigo for s in self.elementos)

    def pendientes(self):
        return list(self.elementos)


# B. Pila LIFO de despachos
class PilaDespachos:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, codigo_operacion, codigo_producto):
        # Agrega el despacho en la cima
        self.elementos.append({"operacion": codigo_operacion,
                               "producto": codigo_producto})

    def desapilar(self):
        # Retira el último despacho (None si está vacía)
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def cima(self):
        return None if self.esta_vacia() else self.elementos[-1]

    def existe(self, codigo_operacion):
        return any(d["operacion"] == codigo_operacion for d in self.elementos)

    def consultar(self):
        # Devuelve los despachos de la cima a la base
        return list(reversed(self.elementos))


# C. Árbol binario de búsqueda de productos
class Nodo:
    def __init__(self, codigo):
        self.codigo = codigo
        self.izquierdo = None
        self.derecho = None


class ArbolProductos:
    def __init__(self):
        self.raiz = None

    def insertar(self, codigo):
        # Inserta el código; False si ya existe
        if self.raiz is None:
            self.raiz = Nodo(codigo)
            return True
        actual = self.raiz
        while True:
            if codigo == actual.codigo:
                return False
            if codigo < actual.codigo:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(codigo)
                    return True
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(codigo)
                    return True
                actual = actual.derecho

    def buscar(self, codigo):
        # Devuelve si existe y los nodos visitados
        camino = []
        actual = self.raiz
        while actual is not None:
            camino.append(actual.codigo)
            if codigo == actual.codigo:
                return True, camino
            actual = actual.izquierdo if codigo < actual.codigo else actual.derecho
        return False, camino

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.codigo)
            self._inorden(nodo.derecho, resultado)

    def eliminar(self, codigo):
        # Elimina el código; False si no existía
        existe, _ = self.buscar(codigo)
        if not existe:
            return False
        self.raiz = self._eliminar(self.raiz, codigo)
        return True

    def _eliminar(self, nodo, codigo):
        if nodo is None:
            return None
        if codigo < nodo.codigo:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, codigo)
        elif codigo > nodo.codigo:
            nodo.derecho = self._eliminar(nodo.derecho, codigo)
        else:
            # Hoja o un solo hijo: se reemplaza por su hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            # Dos hijos: se reemplaza por el sucesor inorden
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo
            nodo.codigo = sucesor.codigo
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.codigo)
        return nodo

    def dibujar(self):
        # Dibuja el árbol en texto (raíz a la izquierda)
        lineas = []
        self._dibujar(self.raiz, 0, lineas)
        return "\n".join(lineas) if lineas else "(árbol vacío)"

    def _dibujar(self, nodo, nivel, lineas):
        if nodo is not None:
            self._dibujar(nodo.derecho, nivel + 1, lineas)
            lineas.append("      " * nivel + str(nodo.codigo))
            self._dibujar(nodo.izquierdo, nivel + 1, lineas)


# Datos iniciales obligatorios
def cargar_datos_iniciales(cola, pila, arbol):
    for i, codigo in enumerate(["P001", "P002", "P003"]):
        cola.encolar(codigo, ESTUDIANTES[i % len(ESTUDIANTES)])
    for operacion, producto in [("D001", 50), ("D002", 70), ("D003", 30)]:
        pila.apilar(operacion, producto)
    for codigo in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(codigo)


# Validación de entradas
def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  [!] El valor no puede estar vacío.")


def leer_codigo(mensaje, prefijo):
    # Lee un código tipo P004 o D004
    while True:
        valor = input(mensaje).strip().upper()
        if len(valor) > 1 and valor[0] == prefijo and valor[1:].isdigit():
            return valor
        print(
            f"  [!] Formato inválido. Use '{prefijo}' seguido de números (ej. {prefijo}004).")


def leer_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if numero > 0:
                return numero
            print("  [!] El código debe ser un número entero positivo.")
        except ValueError:
            print("  [!] Debe ingresar un número entero.")


# Menús
def menu_cola(cola):
    while True:
        print("\n--- A. Solicitudes (Cola FIFO) ---")
        print("1. Registrar solicitud")
        print("2. Atender siguiente solicitud")
        print("3. Mostrar solicitudes pendientes")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            codigo = leer_codigo("Código de solicitud (ej. P004): ", "P")
            if cola.existe(codigo):
                print(f"  [!] La solicitud {codigo} ya está en la cola.")
                continue
            cliente = leer_texto("Nombre del cliente: ")
            cola.encolar(codigo, cliente)
            print(f"  Solicitud {codigo} agregada al final de la cola.")
        elif opcion == "2":
            atendida = cola.atender()
            if atendida is None:
                print("  [!] No existen solicitudes para atender.")
            else:
                print(
                    f"  Atendida: {atendida['codigo']} - {atendida['cliente']}")
        elif opcion == "3":
            pendientes = cola.pendientes()
            if not pendientes:
                print("  No hay solicitudes pendientes.")
            else:
                print("  Pendientes (primero a último):")
                for pos, s in enumerate(pendientes, 1):
                    print(f"   {pos}. {s['codigo']} - {s['cliente']}")
        elif opcion == "0":
            return
        else:
            print("  [!] Opción inválida.")


def menu_pila(pila):
    while True:
        print("\n--- B. Despachos (Pila LIFO) ---")
        print("1. Registrar despacho")
        print("2. Consultar despachos registrados")
        print("3. Retirar último despacho (desapilar)")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            operacion = leer_codigo("Código de operación (ej. D004): ", "D")
            if pila.existe(operacion):
                print(f"  [!] El despacho {operacion} ya está registrado.")
                continue
            producto = leer_entero("Código de producto: ")
            pila.apilar(operacion, producto)
            print(f"  Despacho {operacion} apilado en la cima.")
        elif opcion == "2":
            despachos = pila.consultar()
            if not despachos:
                print("  No hay despachos registrados.")
            else:
                print("  Despachos (cima a base):")
                for d in despachos:
                    print(f"   {d['operacion']} - producto {d['producto']}")
        elif opcion == "3":
            retirado = pila.desapilar()
            if retirado is None:
                print("  [!] La pila está vacía: no hay despachos para retirar.")
            else:
                print(f"  Retirado (corrección de registro): {retirado['operacion']}"
                      f" - producto {retirado['producto']}")
        elif opcion == "0":
            return
        else:
            print("  [!] Opción inválida.")


def menu_arbol(arbol):
    while True:
        print("\n--- C. Productos (Árbol binario de búsqueda) ---")
        print("1. Insertar código")
        print("2. Buscar código")
        print("3. Mostrar recorrido inorden")
        print("4. Eliminar código")
        print("5. Dibujar árbol")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            codigo = leer_entero("Código a insertar: ")
            if arbol.insertar(codigo):
                print(f"  Código {codigo} insertado.")
            else:
                print(f"  [!] El código {codigo} ya existe.")
        elif opcion == "2":
            codigo = leer_entero("Código a buscar: ")
            existe, camino = arbol.buscar(codigo)
            estado = "EXISTE" if existe else "NO existe"
            print(f"  El código {codigo} {estado}. Nodos visitados: {camino}")
        elif opcion == "3":
            codigos = arbol.inorden()
            print(f"  Inorden: {codigos if codigos else '(árbol vacío)'}")
        elif opcion == "4":
            codigo = leer_entero("Código a eliminar: ")
            if arbol.eliminar(codigo):
                print(
                    f"  Código {codigo} eliminado. Inorden: {arbol.inorden()}")
            else:
                print(f"  [!] El código {codigo} no existe en el árbol.")
        elif opcion == "5":
            print(arbol.dibujar())
        elif opcion == "0":
            return
        else:
            print("  [!] Opción inválida.")


def resumen(cola, pila, arbol):
    # Muestra el estado de las tres estructuras
    print("\n=== Estado general del sistema ===")
    print("Cola (primero a último):", [s["codigo"] for s in cola.pendientes()])
    print("Pila (cima a base):     ", [
          d["operacion"] for d in pila.consultar()])
    print("Árbol (inorden):        ", arbol.inorden())


def despachar(cola, pila, arbol, producto):
    # Atiende la siguiente solicitud y apila su despacho
    # Devuelve (solicitud, operacion) o (None, None) si no se pudo
    existe, _ = arbol.buscar(producto)
    if cola.esta_vacia() or not existe:
        return None, None
    solicitud = cola.atender()
    operacion = f"D{len(pila.elementos) + 1:03d}"
    while pila.existe(operacion):
        operacion = f"D{int(operacion[1:]) + 1:03d}"
    pila.apilar(operacion, producto)
    return solicitud, operacion


def atender_y_despachar(cola, pila, arbol):
    # Atiende una solicitud, valida el producto y registra el despacho
    if cola.esta_vacia():
        print("  [!] No existen solicitudes para atender.")
        return
    producto = leer_entero("Código de producto solicitado: ")
    solicitud, operacion = despachar(cola, pila, arbol, producto)
    if solicitud is None:
        print(
            f"  [!] El producto {producto} no existe. La solicitud sigue en cola.")
        return
    print(f"  Solicitud {solicitud['codigo']} ({solicitud['cliente']}) atendida;"
          f" despacho {operacion} registrado para el producto {producto}.")


# Pruebas automáticas
def con_entradas(valores, funcion, *args):
    # Ejecuta una función de lectura simulando lo que escribe el usuario
    entradas = iter(valores)
    original = builtins.input
    builtins.input = lambda mensaje="": next(entradas)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            return funcion(*args)
    finally:
        builtins.input = original


def ejecutar_pruebas():
    print("\n=== Pruebas automáticas ===")
    resultados = []

    def verificar(descripcion, condicion):
        resultados.append(condicion)
        estado = "OK   " if condicion else "FALLO"
        print(f"  [{estado}] {descripcion}")

    # A. Cola FIFO (estructura nueva, no afecta los datos del menú)
    print("\nA. Cola FIFO de solicitudes")
    cola = ColaSolicitudes()
    verificar("Cola nueva está vacía", cola.esta_vacia())
    verificar("Atender cola vacía devuelve None (control)",
              cola.atender() is None)
    for i, codigo in enumerate(["P001", "P002", "P003"]):
        cola.encolar(codigo, ESTUDIANTES[i])
    verificar("Registra solicitudes con código y nombre de estudiante",
              cola.pendientes()[0] == {"codigo": "P001", "cliente": "Stanley"})
    cola.encolar("P004", "Ortiz")
    verificar("Nueva solicitud P004 queda al final de la cola",
              cola.pendientes()[-1]["codigo"] == "P004")
    verificar("Detecta código de solicitud repetido", cola.existe("P002"))
    orden = [cola.atender()["codigo"] for _ in range(4)]
    verificar(f"Atiende en orden de llegada {orden}",
              orden == ["P001", "P002", "P003", "P004"])
    verificar("Sin pendientes tras atender todo", cola.pendientes() == [])

    # B. Pila LIFO
    print("\nB. Pila LIFO de despachos")
    pila = PilaDespachos()
    verificar("Desapilar pila vacía devuelve None (control)",
              pila.desapilar() is None)
    for operacion, producto in [("D001", 50), ("D002", 70), ("D003", 30)]:
        pila.apilar(operacion, producto)
    verificar("Registra despacho con operación y producto",
              pila.cima() == {"operacion": "D003", "producto": 30})
    consulta = [d["operacion"] for d in pila.consultar()]
    verificar(f"Consulta de cima a base {consulta}",
              consulta == ["D003", "D002", "D001"])
    verificar("Desapila primero el último registrado (D003)",
              pila.desapilar()["operacion"] == "D003")
    verificar("Luego desapila D002", pila.desapilar()["operacion"] == "D002")
    pila.desapilar()
    verificar("Pila queda vacía y desapilar devuelve None",
              pila.esta_vacia() and pila.desapilar() is None)

    # C. Árbol binario de búsqueda
    print("\nC. Árbol binario de búsqueda de productos")
    arbol = ArbolProductos()
    for codigo in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(codigo)
    verificar("Raíz del árbol es 50", arbol.raiz.codigo == 50)
    verificar("Menores a la izquierda y mayores a la derecha",
              arbol.raiz.izquierdo.codigo == 30 and arbol.raiz.derecho.codigo == 70)
    verificar("Inorden sale ordenado [20, 30, 40, 50, 60, 70, 80]",
              arbol.inorden() == [20, 30, 40, 50, 60, 70, 80])
    verificar("No permite insertar código duplicado (50)",
              not arbol.insertar(50))
    existe, camino = arbol.buscar(60)
    verificar(f"Busca 60: existe, camino {camino}",
              existe and camino == [50, 70, 60])
    existe, _ = arbol.buscar(99)
    verificar("Busca 99: no existe", not existe)
    arbol.eliminar(20)
    verificar("Elimina hoja 20, inorden sigue ordenado",
              arbol.inorden() == [30, 40, 50, 60, 70, 80])
    arbol.eliminar(30)
    verificar("Elimina 30 (un hijo), 40 sube a su lugar",
              arbol.raiz.izquierdo.codigo == 40)
    arbol.eliminar(50)
    verificar("Elimina raíz 50 (dos hijos), la reemplaza el sucesor 60",
              arbol.raiz.codigo == 60 and arbol.inorden() == [40, 60, 70, 80])
    verificar("Eliminar código inexistente devuelve False",
              not arbol.eliminar(99))

    # D. Integración y validaciones
    print("\nD. Integración y validaciones")
    cola, pila, arbol = ColaSolicitudes(), PilaDespachos(), ArbolProductos()
    cargar_datos_iniciales(cola, pila, arbol)
    solicitud, _ = despachar(cola, pila, arbol, 99)
    verificar("Producto inexistente: la solicitud sigue en cola y no se apila",
              solicitud is None and len(cola.pendientes()) == 3
              and len(pila.consultar()) == 3)
    solicitud, operacion = despachar(cola, pila, arbol, 60)
    verificar(f"Producto 60: atiende {solicitud['codigo']} y apila {operacion}",
              solicitud["codigo"] == "P001"
              and pila.cima() == {"operacion": "D004", "producto": 60})
    verificar("El árbol no cambia al despachar (estructuras independientes)",
              arbol.inorden() == [20, 30, 40, 50, 60, 70, 80])
    pila.desapilar()
    verificar("Desapilar no altera la cola ni el árbol",
              len(cola.pendientes()) == 2 and len(arbol.inorden()) == 7)
    despachar(cola, pila, arbol, 20)
    despachar(cola, pila, arbol, 80)
    solicitud, _ = despachar(cola, pila, arbol, 50)
    verificar("Cola vacía: no se registra despacho",
              solicitud is None and pila.cima()["producto"] == 80)
    verificar("Rechaza código vacío o mal formado ('', 'X1', 'P') y acepta 'p004'",
              con_entradas(["", "X1", "P", "p004"], leer_codigo, "> ", "P") == "P004")
    verificar("Rechaza 'abc', '-3' y '0' y acepta 25",
              con_entradas(["abc", "-3", "0", "25"], leer_entero, "> ") == 25)
    verificar("Rechaza nombre vacío y acepta 'Ken'",
              con_entradas(["", "   ", "Ken"], leer_texto, "> ") == "Ken")

    aprobadas = sum(resultados)
    print(f"\n  Resultado: {aprobadas}/{len(resultados)} pruebas aprobadas.")


def menu_principal():
    cola, pila, arbol = ColaSolicitudes(), PilaDespachos(), ArbolProductos()
    cargar_datos_iniciales(cola, pila, arbol)
    while True:
        print("\n===== Distribuidora 'Las naranjas' =====")
        print("1. Solicitudes (Cola FIFO)")
        print("2. Despachos (Pila LIFO)")
        print("3. Productos (Árbol binario de búsqueda)")
        print("4. Atender solicitud y registrar despacho (integrado)")
        print("5. Ver estado general")
        print("6. Ejecutar pruebas automáticas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            menu_cola(cola)
        elif opcion == "2":
            menu_pila(pila)
        elif opcion == "3":
            menu_arbol(arbol)
        elif opcion == "4":
            atender_y_despachar(cola, pila, arbol)
        elif opcion == "5":
            resumen(cola, pila, arbol)
        elif opcion == "6":
            ejecutar_pruebas()
        elif opcion == "0":
            print("Programa finalizado.")
            return
        else:
            print("  [!] Opción inválida. Ingrese un número del 0 al 6.")


if __name__ == "__main__":
    try:
        menu_principal()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
