from datetime import datetime
from typing import List
from domain.entities.pedido import Pedido
from domain.entities.detalle_pedido import DetallePedido
from domain.entities.producto import Producto

class VentasMock:
    """
    Simula el comportamiento del módulo de ventas.

    Este mock actúa como una capa de persistencia en memoria
    para pedidos y productos.

    Attributes:
        pedidos (List[Pedido]): Lista de pedidos simulados.
        productos (List[Producto]): Catálogo de productos disponible.
    """

    pedidos: List[Pedido] = []
    productos: List[Producto] = [
        Producto(1, "Laptop", 3500),
        Producto(2, "Mouse", 80)
    ]

    @classmethod
    def crear_pedido(cls) -> Pedido:
        """
        Crea un pedido con datos simulados.

        Returns:
            Pedido: Pedido generado en memoria.
        """
        pedido = Pedido(
            id=len(cls.pedidos) + 1,
            fecha=datetime.now(),
            estado="pendiente"
        )

        detalle = DetallePedido(cls.productos[0], 1)
        pedido.agregar_detalle(detalle)

        cls.pedidos.append(pedido)
        return pedido

    @classmethod
    def obtener_pedidos(cls) -> List[Pedido]:
        """
        Retorna todos los pedidos simulados.

        Returns:
            List[Pedido]: Lista de pedidos.
        """
        return cls.pedidos