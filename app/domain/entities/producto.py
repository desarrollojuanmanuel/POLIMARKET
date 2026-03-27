from dataclasses import dataclass

@dataclass
class Producto:
    """
    Representa un producto disponible para la venta.

    Attributes:
        id (int): Identificador único del producto.
        nombre (str): Nombre descriptivo del producto.
        precio (float): Precio unitario actual del producto.
    """

    id: int
    nombre: str
    precio: float

    def actualizar_precio(self, nuevo_precio: float) -> None:
        """
        Actualiza el precio del producto.

        Args:
            nuevo_precio (float): Nuevo valor del producto.

        Raises:
            ValueError: Si el precio es menor o igual a cero.
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self.precio = nuevo_precio