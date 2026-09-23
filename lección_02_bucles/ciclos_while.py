#Sintaxis del ciclo while
# numero = int(input('Escriba un número positivo: '))
# while numero <= 0:
#     print('Ha escrito un número negativo! Inténtelo de nuevo...' )
#     numero = int(input('Escriba un número positivo: '))
# print('Gracias por su colaboración!!..')

#Casos de bucles infinitos
#Definir una variable
# i = 1
##Ejecutar este ciclo mientras i es menor que 15, pero el valor de i no se modifica, nunca cambia
# while i < 15:
#     print('Hola Mundo!!')
#     i += 1

#El valor de i puede cambiar, pero la condición nunca es falsa
# i = 1
# while i != 100:
#     print(i, end=' ')
#     i += 1

#Aumentando el contador o variable de control
# contador = 0
# while contador <= 5:
#     print('Estoy en un loop')
#     print('Hacer loop es aloopcinante..')
#     contador = contador + 1

#Romper el ciclo while
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break

#Iterar sobre una lista mediante while
# lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# i = 0
# while i < len(lenguajes):
#     print(lenguajes[i])
#     i += 1

#Cómo crear un ciclo infinito con while True
while True:
    valor_ingresado = int(input('Ingrese un número entero: '))
    if valor_ingresado % 2 != 0:
        print('Este número es impar..')
        break
    print('Este número es par..')
