import pytest
from stockguard.models import Item


class TestItem:
    def test_creacion_valida(self):
        item = Item(name="Laptop", qty=10, price=999.99)
        assert item.name == "Laptop"
        assert item.qty == 10
        assert item.price == 999.99

    def test_valueerror_qty_cero(self):
        with pytest.raises(ValueError):
            Item(name="Mouse", qty=0, price=25.0)

    def test_valueerror_qty_negativo(self):
        with pytest.raises(ValueError):
            Item(name="Mouse", qty=-5, price=25.0)

    def test_valueerror_price_cero(self):
        with pytest.raises(ValueError):
            Item(name="Mouse", qty=5, price=0)

    def test_valueerror_price_negativo(self):
        with pytest.raises(ValueError):
            Item(name="Mouse", qty=5, price=-1)

    def test_edge_case_precio_minimo(self):
        item = Item(name="Tornillo", qty=100, price=0.001)
        assert item.price == 0.001
        assert item.qty == 100

    def test_edge_case_qty_muy_grande(self):
        item = Item(name="Arena", qty=10**9, price=0.01)
        assert item.qty == 10**9
