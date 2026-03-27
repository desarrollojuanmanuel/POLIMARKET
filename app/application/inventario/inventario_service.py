from infrastructure.mocks.inventario_mock import InventarioMock


class InventarioService:

    @staticmethod
    def consultar_stock(producto_id: int):
        return InventarioMock.consultar_stock(producto_id)
    
    @staticmethod
    def actualizar_stock(producto_id: int, cantidad: int):
        InventarioMock.actualizar_stock(producto_id, cantidad)
        return InventarioMock.consultar_stock(producto_id)