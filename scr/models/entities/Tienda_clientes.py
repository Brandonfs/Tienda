class Tienda_clientes:
    def __init__(self,nombre, apellido, email, password, clienteId=None):
        self.clienteId = clienteId
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        