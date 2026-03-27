class RRHHMock:
    """
    Simula la gestión de vendedores y autorizaciones.

    Attributes:
        vendedores (dict): Información básica de vendedores.
    """

    vendedores = {
        1: {"nombre": "Juan", "estado": "activo"},
        2: {"nombre": "Pedro", "estado": "inactivo"}
    }

    @classmethod
    def validar_vendedor(cls, vendedor_id: int) -> bool:
        """
        Valida si un vendedor está activo.

        Args:
            vendedor_id (int): ID del vendedor.

        Returns:
            bool: True si está activo, False en caso contrario.
        """
        vendedor = cls.vendedores.get(vendedor_id)
        return vendedor is not None and vendedor["estado"] == "activo"