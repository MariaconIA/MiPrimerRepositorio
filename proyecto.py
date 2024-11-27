import os #crear directorios

CARPETA = 'contactos/' #carpetas de cont
EXTENSION = '.TXT' #EXTENSION DEL ARCHIVO

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre= nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
#REVISA SI LA CARPETA EXISTE O NO
    crear_directorio()

#Muestra el menu de opciones
    mostrar_menu()

#preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

    #Ejecutar las opciones

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False   
        else:
            print('Opcion no válida, intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea Eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado Correctamente!')
    except expression as identifier:
        print('No existe ese contacto')
    app()
    
def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print('\r\n')

    app()

def mostrar_contactos():
    print('Lista de archivos creados \r\n')
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
#imprime un separador entre contenidos
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    #Revisar si el nombre existe antes de modificarlo
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        with open (CARPETA + nombre_anterior + EXTENSION, 'w') as archivo: # ventaja que no es necesario cerrar el archivo
            nombre_contacto = input('Agrega el nuevo nombre:\r\n')
            telefono_contacto = input('Agrega el nuevo numero de teléfono:\r\n')
            categoria_contacto = input('Agrega la nueva categoria contacto:\r\n')

            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n') 
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')   

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mensaje de exito
        print('\r\nContacto ha sido actualizado\r\n')
    else:
        print('Ese contacto no existe')
    
    #Reiniciar al app
    app()

def agregar_contacto():
    print('Escribe los datos para agregar los datos')
    nombre_contacto = input('Nombre contacto:\r\n')
#REVISAR SI EL ARCHIVO EXITE
    existe = existe_contacto(nombre_contacto)
    if not existe: 
        with open (CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: # ventaja que no es necesario cerrar el archivo
    #resto de los campos   
            telefono_contacto = input('Agrega el numero de teléfono:\r\n')
            categoria_contacto = input('Agrega categoria contacto:\r\n')

    #instanciar la clase
            contacto =Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n') 
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')           

            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Este contacto, ya existe')

    #Reiniciar al app
    app()


def mostrar_menu():
    print('Seleccione del menu lo que desea hacer')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    
def crear_directorio():
    if not os.path.exists(CARPETA): #si una carpeta no existe crearla
        os.makedirs(CARPETA) #crear la carpeta

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
app()