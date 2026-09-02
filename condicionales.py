#Condicionales
#Utilizar condicionales para verificar si un valor es mayor, menor o igual a otro
# x = 10
# y  10
# if x < y:
#     pr=int('x es menor a y')
# elif x == y:
#     print('x es igual a y')
# else:
#     print('x es mayor a y')

#Evaluar variables booleanas en condicionales
# a = True
# if type(a) == bool:
#     print('a es booleano')
# else:
#     print('a no es booleno')

#Evaluar mediante varias condiciones al mismo tiempo
# a = 13
# b = 12
# c = 11
# if a > b and b > c:
#     print('Ambas condiciones son verdaderas..')
# else:
#     print('Al menos una condición no es verdadera..')

#Condicionales con valores string
# color = 'azul'
# if color == 'verde':
#     print('El color es verde')
# elif color == 'rojo':
#     print('El color es rojo')
# else:
#     print('El color no es verde ni rojo')

# #If anidado
# password = input('Ingrese su contraseña: ')
# if len(password) >= 8:
#     print('Tu contraseña es suficientemente larga..')
#     if password == 'MiClaveSegura':
#         print('Además, es la contraseña correcta..')
#     else:
#         print('Pero es incorrecta..')
# else:
#     print('Tu contraseña es muy corta e insegura..')
#     print('Además, es incorrecta, por supuesto...')    

# clave = 'contraseña'
# password = input('Favor, ingrese la contraseña: ')
# if password.lower() == clave:
#     print('Acceso correcto..')
# else:
#     print('Contraseña incorrecta..')

# dividendo = float(input('Ingrese el primer número (dividendo): '))
# divisor = float(input('Ahora, ingrese el otro número (divisor): '))
# if divisor == 0:
#     print('Error, división por cero..')
# else:
#     print('El resultado de la división es', dividendo/divisor)

numero = int(input('Ingrese el número, veremos si es par o impar: '))
if numero % 2 == 0:
    print('El número es par..') 
else:
    print('Es impar..')