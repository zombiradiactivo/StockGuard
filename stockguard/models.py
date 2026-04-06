from dataclasses import dataclass


@dataclass
class Item:
    """Representa un artículo en el inventario.

    Attributes:
        name: Nombre del artículo.
        qty: Cantidad disponible del artículo.
        price: Precio unitario del artículo.
    """

    name: str
    qty: int
    price: float

    def __post_init__(self) -> None:
        """Inicializa el objeto después de la creación.

        Args:
            None.

        Raises:
            ValueError: Si qty es menor o igual a 0.
            ValueError: Si price es menor o igual a 0.
        """
        if self.qty <= 0:
            raise ValueError("qty debe ser mayor a 0")
        if self.price <= 0:
            raise ValueError("price debe ser mayor a 0")
