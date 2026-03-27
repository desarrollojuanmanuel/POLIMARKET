from dataclasses import dataclass
from datetime import datetime

@dataclass
class Autorizacion:
    """
    Representa el estado de autorización de un vendedor.

    Attributes:
        id (int): Identador único.
        fecha (datetime): Fecha de la autorización.
        estado (str): Estado actual (autorizado, revocado).
    """

    id: int
    fecha: datetime
    estado: str

    def autorizar_vendedor(self) -> None:
        """Autoriza al vendedor."""
        self.estado = "autorizado"

    def revocar_autorizacion(self) -> None:
        """Revoca la autorización del vendedor."""
        self.estado = "revocado"