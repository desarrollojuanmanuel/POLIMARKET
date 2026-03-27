from dataclasses import dataclass
from datetime import datetime

@dataclass
class OrdenEntrega:
    """
    Representa una orden de entrega generada a partir de un pedido.

    Attributes:
        id (int): Identificador de la orden.
        fecha (datetime): Fecha de creación.
        estado (str): Estado de la entrega.
    """

    id: int
    fecha: datetime
    estado: str

    def generar_entrega(self) -> None:
        """
        Marca la orden como generada.
        """
        self.estado = "generada"

    def confirmar_entrega(self) -> None:
        """
        Marca la orden como entregada.
        """
        self.estado = "entregada"