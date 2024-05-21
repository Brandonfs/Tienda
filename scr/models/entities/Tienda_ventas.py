class Tienda_ventas:
    def __init__(self, clienteId,  fechaVenta, total, ventaId=None):
        self.ventaId=ventaId
        self.clienteId=clienteId
        self.fechaVenta=fechaVenta
        self.total=total
        
        