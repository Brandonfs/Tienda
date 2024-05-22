from scr.database.dbconnect import get_connection


class model_Tienda_detallesVentas:

    #    @classmethod :Permite acceder y modificar los atributos de la clase.
    # @staticmethod : No puede acceder ni modificar los atributos de instancia o clase , no recibe referecia self, cls

    @staticmethod
    # Listar
    # Para prevenir la inyección de SQL, es recomendable utilizar consultas parametrizadas o consultas preparadas.
    # Estas técnicas permiten separar claramente los datos de la consulta SQL,
    # evitando así la posibilidad de que los datos ingresados por el usuario se interpreten como parte del código SQL.

    def get_tienda_detallesVentas_list_activos():
        connection = get_connection()
        with connection.cursor() as cursor:
            SQL_SELECT = "SELECT * FROM detallesVentas WHERE CANTIDAD > '1'"
            cursor.execute(SQL_SELECT)
            listDetallesVentas_ctrl = cursor.fetchall()

        return listDetallesVentas_ctrl

    @staticmethod
    # Listar

    def get_tienda_detallesVentas_list_noActivos():
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(SQL_SELECT)
            SQL_SELECT = "SELECT * FROM detallesVentas WHERE CANTIDAD = '0'"
            listDetallesVentasNA_ctrl = cursor.fetchall()

        return listDetallesVentasNA_ctrl

    # Insertar
    @staticmethod
    def add_tienda_detallesVentas(tienda_detallesVentas):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()
        # SQLINJECTION EVITA CON LA CONSULTA PARAMETRIZADA
        SQL_INSERT = "INSERT INTO detallesVentas(DETALLEID, VENTAID, PRODUCTOID, CANTIDAD, " \
                     "PRECIOUNITARIO, SUBTOTAL) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (tienda_detallesVentas.detalleId, tienda_detallesVentas.ventaId, 
                  tienda_detallesVentas.productoId, tienda_detallesVentas.cantidad, 
                  tienda_detallesVentas.precioUnitario, tienda_detallesVentas.subTotal)
                  
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
    def update_tienda_detallesVentas(tienda_detallesVentas):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()
        # El bloque with se asegura de que la conexión se cierre correctamente al finalizar,
        # incluso si ocurren excepciones.
        SQLUPDATE = "UPDATE detallesVentas SET DETALLEID=%s, VENTAID=%s, PRODUCTOID=%s, " \
                "CANTIDAD=%s, PRECIOUNITARIO=%s, SUBTOTAL=%s"
        values = (tienda_detallesVentas.DETALLEID, tienda_detallesVentas.VENTAID, 
                  tienda_detallesVentas.PRODUCTOID, tienda_detallesVentas.CANTIDAD,
                  tienda_detallesVentas.PRECIOUNITARIO, tienda_detallesVentas.SUBTOTAL)
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
    def delete_tienda_detallesVentas(id):
        mi_db = get_connection()
        mi_cursor = mi_db.cursor()

        SQL_DELETE = "DELETE FROM detallesVentas WHERE DetalleId = %s"
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

        SQL_CANCEL = "UPDATE detallesVentas SET cantidad=%s WHERE DetalleId=%s"
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
