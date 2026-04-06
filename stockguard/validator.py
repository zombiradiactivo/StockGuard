def validate_qty(qty: int) -> bool:
    """Valida que la cantidad sea un entero positivo.

    Args:
        qty: Cantidad a validar.

    Returns:
        bool: True si la cantidad es válida, False en caso contrario.

    Raises:
        TypeError: Si qty no es un entero.

    Example:
        >>> validate_qty(10)
        True
        >>> validate_qty(0)
        False
        >>> validate_qty(-5)
        False
    """
    if not isinstance(qty, int):
        raise TypeError("qty debe ser un entero")
    return qty > 0


def validate_price(price: float) -> bool:
    """Valida que el precio sea un número positivo.

    Args:
        price: Precio a validar.

    Returns:
        bool: True si el precio es válido, False en caso contrario.

    Raises:
        TypeError: Si price no es un número (int o float).

    Example:
        >>> validate_price(100.0)
        True
        >>> validate_price(0)
        False
        >>> validate_price(-50.5)
        False
    """
    if not isinstance(price, (int, float)):
        raise TypeError("price debe ser un número")
    return price > 0
