class Tienda_productos:
    def __init__(self,nombre, descripcion, precio, stock, fechaRegistro, id=None):
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.fechaRegistro=fechaRegistro
    