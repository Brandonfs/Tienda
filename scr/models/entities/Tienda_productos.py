class Tienda_productos:
    def __init__(self,nombre, descripcion, precio, stock, fechaRegistro, productoid=None):
        self.productoid=productoid
        self.nombre=nombre
        self.nombre=descripcion
        self.precio=precio
        self.stock=stock
        self.fechaRegistro=fechaRegistro
    