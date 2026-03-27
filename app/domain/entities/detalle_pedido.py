from dataclasses import dataclass
from .producto import Producto

@dataclass
class DetallePedido:
    """
    Representa una línea dentro de un pedido.

    Attributes:
        producto (Producto): Producto asociado al detalle.
        cantidad (int): Cantidad solicitada del producto.
    """

    producto: Producto
    cantidad: int

    def calcular_subtotal(self) -> float:
        """
        Calcula el subtotal del detalle.

        Returns:
            float: Resultado de precio * cantidad.
        """
        return self.producto.precio * self.cantidad