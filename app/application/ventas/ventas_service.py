from infrastructure.mocks.ventas_mock import VentasMock
from infrastructure.mocks.rrhh_mock import RRHHMock

class VentasService:

    @staticmethod
    def crear_pedido(vendedor_id: int):
        if not RRHHMock.validar_vendedor(vendedor_id):
            raise Exception("Vendedor no autorizado")

        return VentasMock.crear_pedido()

    @staticmethod
    def listar_pedidos():
        return VentasMock.obtener_pedidos()