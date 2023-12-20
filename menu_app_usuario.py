from usuario import Usuario
from usuarioDao import UsuarioDao
from logger_base import log

opcion = None

while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios ')
    print('2. Agregar usuarios ')
    print('3. Actualizar usuarios ')
    print('4. Eliminar usuarios ')
    print('5. salir')
    opcion = int(input(f'Selecciona una opción (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe tu nombre de usuario: ')
        password_var = input('Ingresa el password del usuario: ')
        usuario = Usuario(username=username_var,password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input("Escribe el id_usuario a modificar: "))
        username_var = input('Escribe el usuario a actualizar: ')
        password_var = input('Ingresa el password del usuario a actualizar: ')
        usuario = Usuario(id_usuario_var,username_var,password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Selecciona el id de los usuarios a eliminar: '))
        usuario = Usuario(id_usuario_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuario o usuarios eliminados: {usuario}')
else:
    log.info('Salimos de la aplicación...')