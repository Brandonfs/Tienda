class Tienda_detallesVentas:
    def __init__(self, productoId,  cantidad, precioUnitario, ventaId=None):
        self.ventaId=ventaId
        self.productoId=productoId
        self.cantidad=cantidad
        self.precioUnitario=precioUnitario
        
        