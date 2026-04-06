import pytest
from stockguard.validator import validate_qty, validate_price


class TestValidateQty:
    def test_valido_positivo(self):
        assert validate_qty(10) is True
        assert validate_qty(1) is True
        assert validate_qty(1000) is True

    def test_limite_cero(self):
        assert validate_qty(0) is False

    def test_negativo(self):
        assert validate_qty(-1) is False
        assert validate_qty(-100) is False

    def test_mu_alto(self):
        assert validate_qty(10**9) is True
        assert validate_qty(999999999999) is True

    def test_tipo_invalido_string(self):
        with pytest.raises(TypeError):
            validate_qty("10")

    def test_tipo_invalido_float(self):
        with pytest.raises(TypeError):
            validate_qty(10.5)

    def test_edge_case_qty_max_int(self):
        assert validate_qty(2147483647) is True

    def test_edge_case_qty_negativo_gran_magnitud(self):
        assert validate_qty(-2147483648) is False


class TestValidatePrice:
    def test_valido_positivo(self):
        assert validate_price(10.0) is True
        assert validate_price(1) is True
        assert validate_price(0.01) is True

    def test_limite_cero(self):
        assert validate_price(0) is False

    def test_negativo(self):
        assert validate_price(-1.0) is False
        assert validate_price(-100.5) is False

    def test_mu_alto(self):
        assert validate_price(10**9) is True
        assert validate_price(999999999.99) is True

    def test_tipo_invalido_string(self):
        with pytest.raises(TypeError):
            validate_price("10.0")

    def test_tipo_invalido_none(self):
        with pytest.raises(TypeError):
            validate_price(None)

    def test_edge_case_precio_minimo_valido(self):
        assert validate_price(0.001) is True

    def test_edge_case_precio_float_negativo_exacto(self):
        assert validate_price(-0.0) is False
