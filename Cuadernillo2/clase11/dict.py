persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "San Miguel"
}

print(persona)
print(persona["nombre"])

estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "cursos": ["Python", "Estructura de datos"]
}

print(estudiante["nombre"])
estudiante["edad"] = 22
print(estudiante)

# Eliminar con el método del
del estudiante["edad"]

# Eliminar con el método pop
estudiante.pop("nombre")
print(estudiante)