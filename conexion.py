#SI NO ahi conexion exitosa a traves del sys se cierra el programa
import sys
from logger_base import log
#Para trabajar con el pool de conexiones importamos:
from psycopg2 import pool

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Uppercase12.'
    _HOST = '192.168.100.4'
    _DBPORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    #pull de conexiones requiere de indicar el min y maximo num. de objetos de conexiones lo ideal es de 1 a 5
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DBPORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return  cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al realizar la conexión: {e}')
                sys.exit()
                ##en caso de que no sea NONE se hace el pool
        else:
            return cls._pool
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()


    '''conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()'''
