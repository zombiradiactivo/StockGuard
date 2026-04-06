import json
import pytest
from unittest.mock import mock_open, patch, MagicMock
from stockguard.storage import load_inventory, save_inventory


class TestLoadInventory:
    def test_archivo_inexistente(self, mocker):
        mocker.patch('stockguard.storage.os.path.exists', return_value=False)
        result = load_inventory()
        assert result == []

    def test_archivo_corrupto(self, mocker):
        mocker.patch('stockguard.storage.os.path.exists', return_value=True)
        mocker.patch('stockguard.storage.open', mock_open(read_data='{invalid json'))
        result = load_inventory()
        assert result == []

    def test_archivo_vacio(self, mocker):
        mocker.patch('stockguard.storage.os.path.exists', return_value=True)
        mocker.patch('stockguard.storage.open', mock_open(read_data=''))
        result = load_inventory()
        assert result == []

    def test_carga_exitosa(self, mocker):
        data = [{"name": "Item1", "qty": 10, "price": 100.0}]
        mocker.patch('stockguard.storage.os.path.exists', return_value=True)
        mocker.patch('stockguard.storage.open', mock_open(read_data=json.dumps(data)))
        result = load_inventory()
        assert result == data


class TestSaveInventory:
    def test_guardado_con_indent_dos(self, mocker):
        items = [{"name": "Item1", "qty": 10, "price": 100.0}]
        m = mock_open()
        mocker.patch('stockguard.storage.open', m)
        save_inventory(items)
        written_content = ''.join(call[0][0] for call in m().write.call_args_list)
        assert '\n  ' in written_content

    def test_guardado_archivo_vacio(self, mocker):
        m = mock_open()
        mocker.patch('stockguard.storage.open', m)
        save_inventory([])
        m().write.assert_called_once_with('[]')
