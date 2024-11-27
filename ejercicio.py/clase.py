class Restaurant:
#Self se refiere al mismo objeto que se está ejecutando
    def agregar_restaurant(self,nombre):
        self.nombre = nombre #atributo de la clase
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')        
#instanciar clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria Mexico')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('hamburguesas python')
restaurant2.mostrar_informacion()

print(f'Nombre de restaurant: {restaurant.nombre}')
print(f'Nombre de restaurant: {restaurant2.nombre}')