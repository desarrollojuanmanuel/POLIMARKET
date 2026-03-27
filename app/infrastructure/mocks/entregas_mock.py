from datetime import datetime
from typing import List
from domain.entities.orden_entrega import OrdenEntrega

class EntregasMock:
    """
    Simula la gestión de entregas.

    Attributes:
        entregas (List[OrdenEntrega]): Lista de entregas generadas.
    """

    entregas: List[OrdenEntrega] = []

    @classmethod
    def generar_entrega(cls, pedido_id: int) -> OrdenEntrega:
        """
        Genera una orden de entrega simulada.

        Args:
            pedido_id (int): ID del pedido asociado.

        Returns:
            OrdenEntrega: Nueva orden generada.
        """
        entrega = OrdenEntrega(
            id=len(cls.entregas) + 1,
            fecha=datetime.now(),
            estado="generada"
        )

        cls.entregas.append(entrega)
        return entrega