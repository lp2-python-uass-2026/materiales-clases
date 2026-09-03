#Iterar mediante ciclos FOR
#Iterar sobre una lista
#lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for elemento in lenguajes:
#     print(elemento)

#Instrucciones para modificar el flujo de un ciclo FOR
#Haremos que el ciclo se rompa con la primera iteración usando break
# for elemento in lenguajes:
#     break
# print('El ciclo se rompió en la primera iteración..')

#lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
#Romper el ciclo actual si el el elemento es igual a 'C++'
# for elemento in lenguajes:
#     if elemento == 'C++':
#         break
#     print(elemento)

# for elemento in lenguajes:
#     if elemento == 'PHP':
#         print(elemento)
#         break
#     print(elemento)

#Pasar al siguiente elemento de la lista cuando se cumpla una condición usando continue
# lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for elemento in lenguajes:
#     if elemento == 'C++' or elemento == 'PHP':
#         continue
#     print(elemento)

#Iterar sobre una cadena de caracteres
# for letra in 'otorrinolaringología':
#     print(letra)

#Iterar sobre números consecutivos
# for numero in range(1,51):
#     print(numero)

#Cambiar el valor de aumento del rango (por defecto es 1)
# for numero in range(2,201,2):
#     print(numero)

#Disminuir el valor de aumento del rango (por defecto es 1)
# for numero in range(100,0,-1):
#     print(numero)

# for numero in reversed(range(1, 100)):
#     print(numero)

#Otra forma de iterar sobre listas
#lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for index in range(len(lenguajes)):
#     print(f'El lenguaje en la posición {index} es {lenguajes[index]}')

#Iterar sobre diccionarios
lenguajes = {"nombre": "Python", 
             "creador": "Guido van Rossum"
             }

#Imprimir las llaves del diccionario
# for elemento in lenguajes:
#     print(elemento)

# for elemento in lenguajes.keys():
#     print(elemento)

# #Imprimir los valores del diccionario
# for elemento in lenguajes.values():
#     print(elemento)

#Imprimir llave + valor
# for llave, valor in lenguajes.items():
#     print(f'Llave: {llave}, Valor: {valor}')

#Llave + valor, en una tupla
# for elemento in lenguajes.items():
#     print(elemento)

#Algunos ejemplos prácticos resueltos con ciclos FOR
#Ejemplo 1: sumar todos los números de una lista
# numeros = [1, 2, 3, 4, 5]
# suma = 0
# for numero in numeros:
#     suma += numero
# print(f'La suma de los números es: {suma}')

#Ejemplo 2: Encontrar el número más grande de una lista
# numeros = [10, 20, 50, 40, 50]
# maximo = numeros[0]
# for numero in numeros:
#     if numero > maximo:
#         maximo = numero
# print(f'El número más grande de la lista es: {maximo}')

#Ejemplo 3: contar las vocales en una cadena de caracteres
# cadena = 'Hola, mundo!!'
# vocales = 'aeiouAEIOU'
# contador = 0
# for letra in cadena:
#     if letra in vocales:
#         contador += 1
# print(f'La cantidad de vocales en la cadena es: {contador}')
    
#Ejemplo 4: imprimir una tabla de multiplicar
# numero = int(input('Ingrese un número para ver su tabla de multiplicar: '))
# for i in range(1, 11):
#     resultado = numero * i
#     print(f'{numero} x {i} = {resultado}')

#Ejemplo 5: Generar una lista de los primeros 10 números cuadrados
# cuadrados = []
# for i in range(1, 11):
#     cuadrados.append(i ** 2)
# print(f'Los primeros 10 números cuadrados son: {cuadrados}')

#Ejemplo 6: Invertir una cadena
# cadena = 'Python'
# invertida = ''  
# for letra in cadena:
#     invertida = letra + invertida
# print(f'La cadena invertida es: {invertida}')

#Ejemplo 7: Filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []    
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)    
print(f'Los números pares de la lista son: {pares}')

