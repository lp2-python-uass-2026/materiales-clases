# Lección 03: Funciones

## Introducción

A medida que los programas crecen, resulta necesario organizar el código para hacerlo más legible, reutilizable y fácil de mantener.

Las funciones permiten agrupar instrucciones relacionadas bajo un nombre específico, facilitando la reutilización de código y reduciendo la duplicación de instrucciones.

---

## Objetivos de aprendizaje

Al finalizar esta lección serás capaz de:

- Comprender el propósito de las funciones.
- Definir funciones utilizando la palabra clave `def`.
- Invocar funciones desde diferentes partes de un programa.
- Utilizar parámetros y argumentos.
- Retornar valores mediante `return`.
- Diseñar soluciones modulares utilizando funciones.
- Aplicar buenas prácticas en la organización del código.

---

## Contenido de la lección

### Teoría

- `funciones.md`

### Práctica

- `ejercicios_03_funciones.md`

---

## Conceptos clave

### Definición de una función

```python
def saludar():
    print("Hola, mundo")
```

### Llamada a una función

```python
saludar()
```

### Función con parámetros

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
```

### Función con valor de retorno

```python
def sumar(a, b):
    return a + b
```

### Uso del valor retornado

```python
resultado = sumar(5, 3)
print(resultado)
```

---

## ¿Por qué utilizar funciones?

Las funciones ofrecen varias ventajas:

- Evitan la repetición de código.
- Facilitan el mantenimiento de programas.
- Mejoran la legibilidad del código.
- Permiten dividir problemas complejos en tareas más pequeñas.
- Favorecen la reutilización de soluciones.

---

## Recomendaciones

- Ejecuta cada ejemplo y analiza su comportamiento.
- Utiliza nombres descriptivos para las funciones.
- Diseña funciones que realicen una única tarea.
- Practica tanto funciones con parámetros como funciones que retornan valores.
- Resuelve todos los ejercicios propuestos antes de avanzar.

---

## Resultado esperado

Al finalizar esta lección podrás crear funciones propias, reutilizar código y desarrollar programas más organizados, legibles y fáciles de mantener.

---

## Próxima lección

➡️ **Lección 04: JSON**
