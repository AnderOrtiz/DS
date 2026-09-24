materias = ["Programación", "Estructura de Datos", "Base de Datos", "Ingeniería de Software", "Redes"]

print("a) Lista completa de materias:")
print(materias)

materias.append("Matemática Discreta")
materias.append("Sistemas Operativos")
print("\nb) Lista después de agregar 2 materias con append():")
print(materias)

materias.insert(2, "Algoritmos")
print("\nc) Lista después de insertar 'Algoritmos' en la posición 2:")
print(materias)

materias.remove(materias[-1])
print("\nd) Lista después de eliminar la última materia con remove():")
print(materias)

print(f"\ne) Número total de materias: {len(materias)}")