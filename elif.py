#ejemplo con el IF

ocupacion = 'desempleado'

if ocupacion == 'estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'jubilado':
    print('Tienes el 75% de descuento')
elif ocupacion == 'desempleado':
    print('Tienes el 20% de descuento')
else:
    print('Debes pagar el 100%')