# Lección 03 - Soluciones de Ejercicios de Funciones

---

# Ejercicio 1 - Estadísticas de una lista

```python
def estadisticas(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)

    return mayor, menor, promedio


numeros = [10, 20, 30, 40, 50]

mayor, menor, promedio = estadisticas(numeros)

print("Mayor:", mayor)
print("Menor:", menor)
print("Promedio:", promedio)
```

---

# Ejercicio 2 - Buscar un elemento

```python
def buscar(lista, valor):
    return valor in lista


alumnos = ["Ana", "Luis", "Carlos"]

print(buscar(alumnos, "Luis"))
print(buscar(alumnos, "Pedro"))
```

---

# Ejercicio 3 - Eliminar duplicados

```python
def eliminar_duplicados(lista):
    return set(lista)


numeros = [1, 2, 2, 3, 3, 3, 4]

resultado = eliminar_duplicados(numeros)

print(resultado)
```

---

# Ejercicio 4 - Frecuencia de elementos

```python
def contar_frecuencia(lista):
    frecuencias = {}

    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    return frecuencias


datos = ["a", "b", "a", "c", "a", "b"]

print(contar_frecuencia(datos))
```

---

# Ejercicio 5 - Promedio de notas

```python
def calcular_promedio(notas):
    return sum(notas) / len(notas)


def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


notas = [70, 80, 90, 60]

promedio = calcular_promedio(notas)

print("Promedio:", promedio)
print("Estado:", estado(promedio))
```

---

# Ejercicio 6 - Agenda telefónica

```python
agenda = {}


def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    agenda[nombre] = telefono


def buscar_contacto():
    nombre = input("Buscar contacto: ")

    if nombre in agenda:
        print("Teléfono:", agenda[nombre])
    else:
        print("Contacto no encontrado")


def mostrar_contactos():
    for nombre, telefono in agenda.items():
        print(nombre, "-", telefono)


while True:

    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_contacto()

    elif opcion == "2":
        buscar_contacto()

    elif opcion == "3":
        mostrar_contactos()

    elif opcion == "4":
        break

    else:
        print("Opción inválida")
```

---

# Ejercicio 7 - Producto más caro

```python
def producto_mas_caro(productos):
    return max(productos, key=lambda producto: producto[1])


productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000)
]

nombre, precio = producto_mas_caro(productos)

print("Producto:", nombre)
print("Precio:", precio)
```

---

# Ejercicio 8 - Inventario de productos

```python
inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}


def agregar_stock():
    producto = input("Producto: ")

    if producto not in inventario:
        print("Producto no encontrado")
        return

    cantidad = int(input("Cantidad a agregar: "))
    inventario[producto] += cantidad


def vender_producto():
    producto = input("Producto: ")

    if producto not in inventario:
        print("Producto no encontrado")
        return

    cantidad = int(input("Cantidad a vender: "))

    if inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
    else:
        print("Stock insuficiente")


def consultar_stock():
    producto = input("Producto: ")

    if producto in inventario:
        print("Stock disponible:", inventario[producto])
    else:
        print("Producto no encontrado")


while True:

    print("\n1. Agregar stock")
    print("2. Vender producto")
    print("3. Consultar stock")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_stock()

    elif opcion == "2":
        vender_producto()

    elif opcion == "3":
        consultar_stock()

    elif opcion == "4":
        break

    else:
        print("Opción inválida")
```

---

# Ejercicio 9 - Ranking de alumnos

```python
alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]


def mejor_alumno(alumnos):
    return max(alumnos, key=lambda alumno: alumno[1])


def peor_alumno(alumnos):
    return min(alumnos, key=lambda alumno: alumno[1])


def promedio_general(alumnos):
    total = 0

    for nombre, nota in alumnos:
        total += nota

    return total / len(alumnos)


print("Mejor alumno:", mejor_alumno(alumnos))
print("Peor alumno:", peor_alumno(alumnos))
print("Promedio general:", promedio
