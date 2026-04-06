import json
import os
from typing import List


INVENTORY_FILE = 'inventory.json'


def load_inventory() -> List[dict]:
    """Carga el inventario desde el archivo JSON.

    Returns:
        List[dict]: Lista de artículos en el inventario.
        Devuelve lista vacía si el archivo no existe o está corrupto.

    Raises:
        IOError: Si ocurre un error de lectura inesperado.
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTORY_FILE, encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_inventory(items: List[dict]) -> None:
    """Guarda el inventario en el archivo JSON.

    Args:
        items: Lista de artículos a guardar.

    Raises:
        IOError: Si ocurre un error al escribir el archivo.
    """
    with open(INVENTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2)
