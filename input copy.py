nombre = input('Cual es tu nombre? \r\n')

print(f'Hola {nombre}')

pregunta1 = input('Te gusta la musica romantica? \r\n')
pregunta2 = input('Te gusta Ricardo Arjona? \r\n')
pregunta3 = input('Te gusta la cancion de Historia de un taxi? \r\n')

print(f'Tu respuesta a la primera pregunta fue {pregunta1}')
print(f'Tu respuesta a la segunda pregunta fue {pregunta2}')
print(f'Tu respuesta a la tercera pregunta fue {pregunta3}')

edad = input('Cual es tu Edad? \r\n')
#convertir edad string a int
edad = int(edad)
print(f'Ok, tienes {edad} años')

if edad >= 18:
    print('Ya tienes edad para beber')
else:
    print('Aun no tienes edad para beber')

numero = input('Agrega un numero y te dire si es par o no: \r\n')

numero = int(numero)


