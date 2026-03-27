from infrastructure.mocks.entregas_mock import EntregasMock

class EntregaService:

    @staticmethod
    def generar_entrega(pedido_id: int):
        return EntregasMock.generar_entrega(pedido_id)