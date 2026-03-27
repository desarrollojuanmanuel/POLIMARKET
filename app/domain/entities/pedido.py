from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from .detalle_pedido import DetallePedido

@dataclass
class Pedido:
    """
    Representa un pedido realizado por un cliente.

    Attributes:
        id (int): Identificador del pedido.
        fecha (datetime): Fecha de creación del pedido.
        estado (str): Estado actual (pendiente, confirmado, etc.).
        detalles (List[DetallePedido]): Lista de ítems del pedido.
    """

    id: int
    fecha: datetime
    estado: str
    detalles: List[DetallePedido] = field(default_factory=list)

    def agregar_detalle(self, detalle: DetallePedido) -> None:
        """
        Agrega un detalle al pedido.

        Args:
            detalle (DetallePedido): Elemento a agregar.
        """
        self.detalles.append(detalle)

    def calcular_total(self) -> float:
        """
        Calcula el total del pedido.

        Returns:
            float: Suma de todos los subtotales.
        """
        return sum(d.calcular_subtotal() for d in self.detalles)

    def confirmar(self) -> None:
        """
        Cambia el estado del pedido a confirmado.
        """
        self.estado = "confirmado"