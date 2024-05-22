from scr.database.dbconnect import get_connection


class model_Tienda_clientes:

    #    @classmethod :Permite acceder y modificar los atributos de la clase.
    # @staticmethod : No puede acceder ni modificar los atributos de instancia o clase , no recibe referecia self, cls

    @staticmethod
    # Listar
    # Para prevenir la inyección de SQL, es recomendable utilizar consultas parametrizadas o consultas preparadas.
    # Estas técnicas permiten separar claramente los datos de la consulta SQL,
    # evitando así la posibilidad de que los datos ingresados por el usuario se interpreten como parte del código SQL.

    def get_tienda_clientes_list_activos():
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT * FROM clientes WHERE ESTADO = '0'"
            cursor.execute(SQL_SELECT)
            listClientes_ctrl = cursor.fetchall()

        return listClientes_ctrl

    @staticmethod
    # Listar

    def get_tienda_clientes_list_noActivos():
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT * FROM clientes WHERE ESTADO = '1'"
            cursor.execute(SQL_SELECT)
            listClientesNA_ctrl = cursor.fetchall()

        return listClientesNA_ctrl

    # Insertar
    @staticmethod
    def add_tienda_clientes(tienda_clientes):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()
        state = '0'
        # SQLINJECTION EVITA CON LA CONSULTA PARAMETRIZADA
        SQL_INSERT = "INSERT INTO Attention_Control(NOMBRES, APELLIDO, EMAIL, PASSWORD, " \
                     "ROL, ESTADO) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (tienda_clientes.nombres, tienda_clientes.apellido, tienda_clientes.email,
                  tienda_clientes.password, state)
        try:
            mi_cursor.execute(SQL_INSERT, values)
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

        # Actualizar

    @staticmethod
    # En este código, se utilizan marcadores de posición %s en la consulta SQL para indicar dónde se deben
    # insertar los valores. Luego, los valores reales se pasan como una tupla separada (values) en el método execute().
    # Esto garantiza que los valores se traten de forma segura y evita la posibilidad de inyección de SQL.
    def update_tienda_clientes(tienda_clientes):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()
        # El bloque with se asegura de que la conexión se cierre correctamente al finalizar,
        # incluso si ocurren excepciones.
        SQLUPDATE = "UPDATE clientes SET NOMBRE=%s, APELLIDO=%s, EMAIL=%s, PASSWORD=%s, ROL=%s," \
                    " ESTADO=%s, WHERE CLIENTEID=%s"
        values = (tienda_clientes.nombre, tienda_clientes.apellido, tienda_clientes.email,
                  tienda_clientes.password,
                  tienda_clientes.rol, tienda_clientes.estado, tienda_clientes.clienteid)
        try:
            mi_cursor.execute(SQLUPDATE, values)
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

    # Eliminar primer enfoque
    @staticmethod
    def delete_tienda_clientes(id):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()

        SQL_DELETE = "DELETE FROM clientes WHERE ClienteId = %s"
        try:
            mi_cursor.execute(SQL_DELETE, (id,))
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

    # Segundo enfoque de Anulacion
    @staticmethod
    def cancel_tienda_clientes(id):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()

        SQL_CANCEL = "UPDATE clientes SET estado=%s WHERE ClienteId=%s"
        try:
            mi_cursor.execute(SQL_CANCEL, ('ANU', id))
        except:
            mi_db.rollback()
            retorno = 0
        else:
            mi_db.commit()
            retorno = 1
        finally:
            mi_db.close()
            return retorno

    # crud
