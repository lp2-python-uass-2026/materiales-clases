#Uso de condicionales en Python
#Utilizar condicionales para verificar si un valor es mayor, menor o igual a otro
# x = 3
# y = 5
# if x < y:
#     print('x es menor a y')
# elif x == y:
#     print('x e y son iguales')
# else: 
#     print('x es mayor a y')

#Evaluar variables booleanas en condicionales
# a = True
# if a:
#     print('a es verdadero')
# else:
#     print('a es falso')

#Evaluar si una variable es booleana
# a = 3
# if type(a) is bool:
#     print('a es una variable booleana')
# else:
#     print('a es otro tipo de variable, no es booleana')

#Evaluar varias condiciones al mismo tiempo
# a = 10
# b = 5
# c = 5
# if a>b and b>c:
#     print('Ambas condiciones son verdaderas')
# else:
#     print('Al menos una condición no es verdadera')

#Condicionales con valores string
# color = 'verde'
# if color == 'verde':
#     print('El color es verde')
# elif color == 'rojo':
#     print('El color es rojo')
# else:
#     print('Color diferente a verde o rojo')

#If anidado
password = input('Ingrese la contraseña: ')
if (len(password)>=8):
    print(('Tu contraseña es lo suficientemente larga..'))
    if (password == 'miClaveSegura'):
        print('Además, es la contraseña correcta..')
    else:
        print('Pero es incorrecta..')
else:
    print('Tu contraseña es muy corta e insegura..')
    print('Además, es incorrecta (por supuesto)..')