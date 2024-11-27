playlist = {} #Diccionario vacio
playlist ['canciones'] = [] #Lista vacia de canciones

#funcion principal
def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como desea nombrar la playlist')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        #preguntar al usuario por la cancion
        nombre_playlist = playlist['nombre']
        pregunta = f'Agregar canciones para la playlist {nombre_playlist}'
        pregunta += 'Escribe "X" para dejar de agregar canciones' 
        cancion = input(pregunta)

     
app()