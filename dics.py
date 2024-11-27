cancion = {
    'artista' : 'Ricardo arjona',
    'cancion' : 'Del otro lado del sol',
    'lanzamiento': 1992,
    'likes' : 2000
}
#acceder a los elementos del diccionario
print(cancion ['artista'])

artista = cancion['artista']

print(f'Estoy escuchando a {artista}')

#agregar nuevos valores
cancion['playlist'] = 'Romanticas'
print(cancion)

del cancion['lanzamiento']
print(cancion)