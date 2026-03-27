class ProveedoresMock:
    """
    Simula la interacción con proveedores.

    Permite abastecer inventario sin dependencia externa.
    """

    @classmethod
    def abastecer(cls, inventario_mock, producto_id: int, cantidad: int) -> None:
        """
        Incrementa el stock de un producto.

        Args:
            inventario_mock: Referencia al mock de inventario.
            producto_id (int): ID del producto.
            cantidad (int): Cantidad a agregar.
        """
        inventario_mock.actualizar_stock(producto_id, cantidad)