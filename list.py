lenguajes = ['python','kotlin','java','javascript']
             
print(lenguajes[0])

lenguajes.sort()

print(lenguajes)

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Agregar elementos a un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#Agregar elementos a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar un arreglo list
del lenguajes[1]
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('java')
print(lenguajes)