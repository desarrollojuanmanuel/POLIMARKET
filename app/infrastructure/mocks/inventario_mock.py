class InventarioMock:
    """
    Simula el manejo de inventario en memoria.

    Attributes:
        stock (dict): Diccionario con producto_id como clave y cantidad como valor.
    """

    stock = {
        1: 10,
        2: 50
    }

    @classmethod
    def consultar_stock(cls, producto_id: int) -> int:
        """
        Consulta el stock disponible de un producto.

        Args:
            producto_id (int): ID del producto.

        Returns:
            int: Cantidad disponible.
        """
        return cls.stock.get(producto_id, 0)

    @classmethod
    def actualizar_stock(cls, producto_id: int, cantidad: int) -> None:
        """
        Actualiza el stock de un producto.

        Args:
            producto_id (int): ID del producto.
            cantidad (int): Cantidad a sumar/restar.
        """
        cls.stock[producto_id] = cls.stock.get(producto_id, 0) + cantidad