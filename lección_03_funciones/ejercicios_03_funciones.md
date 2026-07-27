# Lección 03 - Ejercicios de Funciones

## Objetivos

Al finalizar estos ejercicios el estudiante será capaz de:

- Crear funciones utilizando `def`.
- Utilizar parámetros y valores de retorno.
- Trabajar con listas, tuplas, conjuntos y diccionarios.
- Resolver problemas de manera modular.
- Reutilizar código mediante funciones.

---

# Ejercicio 1 - Estadísticas de una lista

Crear una función llamada:

```python
estadisticas(numeros)
```

que reciba una lista de números y retorne:

- El valor máximo.
- El valor mínimo.
- El promedio.

## Ejemplo

```python
numeros = [10, 20, 30, 40, 50]
```

### Salida esperada

```text
Mayor: 50
Menor: 10
Promedio: 30
```

---

# Ejercicio 2 - Buscar un elemento

Crear una función:

```python
buscar(lista, valor)
```

que reciba una lista y un valor.

La función debe retornar:

- `True` si el valor existe.
- `False` si el valor no existe.

## Ejemplo

```python
alumnos = ["Ana", "Luis", "Carlos"]
```

```python
buscar(alumnos, "Luis")
```

### Resultado

```text
True
```

---

# Ejercicio 3 - Eliminar duplicados

Crear una función:

```python
eliminar_duplicados(lista)
```

que reciba una lista y retorne una colección sin elementos repetidos utilizando un conjunto (`set`).

## Ejemplo

```python
[1, 2, 2, 3, 3, 3, 4]
```

### Resultado

```python
{1, 2, 3, 4}
```

---

# Ejercicio 4 - Frecuencia de elementos

Crear una función:

```python
contar_frecuencia(lista)
```

que reciba una lista y retorne un diccionario indicando cuántas veces aparece cada elemento.

## Ejemplo

```python
["a", "b", "a", "c", "a", "b"]
```

### Resultado

```python
{
    "a": 3,
    "b": 2,
    "c": 1
}
```

---

# Ejercicio 5 - Promedio de notas

Crear una función:

```python
calcular_promedio(notas)
```

que reciba una lista de notas y retorne el promedio.

Crear también una función:

```python
estado(promedio)
```

que indique:

- "Aprobado" si el promedio es mayor o igual a 60.
- "Reprobado" en caso contrario.

## Ejemplo

```python
notas = [70, 80, 90, 60]
```

### Salida esperada

```text
Promedio: 75
Estado: Aprobado
```

---

# Ejercicio 6 - Agenda telefónica

Utilice un diccionario para almacenar contactos.

Ejemplo:

```python
agenda = {
    "Juan": "098111111",
    "Ana": "098222222"
}
```

Crear las siguientes funciones:

```python
agregar_contacto()
buscar_contacto()
mostrar_contactos()
```

El programa debe mostrar el siguiente menú:

```text
1. Agregar contacto
2. Buscar contacto
3. Mostrar contactos
4. Salir
```

---

# Ejercicio 7 - Producto más caro

Dada la siguiente lista de tuplas:

```python
productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000)
]
```

Crear una función:

```python
producto_mas_caro(productos)
```

que retorne el nombre y precio del producto más caro.

### Salida esperada

```text
Producto: Monitor
Precio: 1200000
```

---

# Ejercicio 8 - Inventario de productos

Utilizando el siguiente diccionario:

```python
inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}
```

Crear las siguientes funciones:

```python
agregar_stock()
vender_producto()
consultar_stock()
```

El programa debe permitir:

- Aumentar el stock de un producto.
- Registrar una venta.
- Consultar la cantidad disponible.

---

# Ejercicio 9 - Ranking de alumnos

Dada la siguiente lista de tuplas:

```python
alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]
```

Crear funciones para:

- Obtener el mejor alumno.
- Obtener el peor alumno.
- Calcular el promedio general.

### Salida esperada

```text
Mejor alumno: Ana (95)
Peor alumno: Pedro (70)
Promedio general: 83.33
```

---

# Ejercicio 10 - Sistema de gestión de estudiantes

Utilizando un diccionario:

```python
estudiantes = {
    "Juan": [70, 80, 90],
    "Ana": [100, 95, 90]
}
```

Crear las siguientes funciones:

```python
agregar_estudiante()
calcular_promedio()
mostrar_promedios()
mejor_estudiante()
```

El programa debe mostrar el siguiente menú:

```text
1. Agregar estudiante
2. Mostrar promedios
3. Mostrar mejor estudiante
4. Salir
```

## Requisitos

- Utilizar funciones para cada operación.
- Utilizar estructuras de datos adecuadas.
- Evitar la repetición de código.
- Validar las entradas del usuario cuando sea necesario.

---

# Desafío Extra (Opcional)

Crear un programa que permita registrar votos utilizando un diccionario.

Cada votante ingresa el nombre de un candidato.

Al finalizar, el programa debe mostrar:

- Cantidad de votos por candidato.
- Candidato ganador.
- Total de votos registrados.

Utilice funciones para organizar la solución.
