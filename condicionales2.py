#Operadores and y or

usuario_logueado = True
usuario_admin = False

if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciario sesión')