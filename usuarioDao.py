from cursorDelPool import CursorDelPool
from usuario import Usuario
from  logger_base import log


class UsuarioDao:
    '''
    DAO DATA ACCESS OBJECT
    CRUD CREATE, READ, UPDATE, DELETE
    '''

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('SEleccionando usuarios')
            cursor.execute(cls._SELECCIONAR)
            #convertir objetos a tipo usuario
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)   #append agrega el usuario
            return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Valores insertados: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount



if __name__ == '__main__':
    #seleccionar
    #usuarios = UsuarioDao.seleccionar()
    #for usuarios in usuarios:
     #   log.debug(usuarios)

    #insertar usuario
    usuario1 = Usuario(id_usuario='',username='ajaimes',password='AnelizHermosa')
    usuarios_insertados = UsuarioDao.insertar(usuario1)
    log.debug(f'Usuarios insertados: {usuarios_insertados}')

    #actualizar usuario:
    #usuario1 = Usuario(1,'aaguirre','1985')
    #usuario_actualizado = UsuarioDao.actualizar(usuario1)
    #log.debug(f'Usuario actualizado {usuario_actualizado}')

    #eliminar usuario
    usuario1 = Usuario(id_usuario=1)
    usuarios_eliminado = UsuarioDao.eliminar(usuario1)
    log.debug(f'Usuarios eliminados: {usuarios_eliminado}')

