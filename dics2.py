#iniciario un diccionario vacio

jugador = {}
print(jugador)

# se une un jugador
jugador['nombre'] = 'Juan'
jugador['puntaje'] = '100'

print(jugador)

#Acceder a un valor
print(jugador.get('consola', 'no existe ese valor'))

for llave, valor in jugador.items():
    print(valor)
del jugador['nombre']
del jugador['puntaje']
print(jugador)