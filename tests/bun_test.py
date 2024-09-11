import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, expected_name",
        [
            ("Флюоресцентная булка R2-D3", "Флюоресцентная булка R2-D3"),
            ("Краторная булка N-200i", "Краторная булка N-200i")
        ],
    )
    def test_get_name(self, name, expected_name):
        bun = Bun(name, 988.0)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize(
        "price, expected_price",
        [
            (988.0, 988.0),
            (1255.0, 1255.0)
        ],
    )
    def test_get_price(self, price, expected_price):
        bun = Bun("Флюоресцентная булка R2-D3", price)
        assert bun.get_price() == expected_price

    def test_mock_name(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988.0)
        new_name = "Солнечная булка"

        bun.get_name = Mock(return_value=new_name)

        assert bun.get_name() == new_name
        bun.get_name.assert_called_once()

    def test_mock_price(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988.0)
        new_price = 1000.0

        bun.get_price = Mock(return_value=new_price)

        assert bun.get_price() == new_price
        bun.get_price.assert_called_once()

    @pytest.mark.parametrize(
        "name, expected_type_name",
        [
            ("Флюоресцентная булка R2-D3", str),
            ("Краторная булка N-200i", str),
        ],
    )
    def test_name_type(self, name, expected_type_name):
        bun = Bun(name, 988.0)
        assert isinstance(bun.get_name(), expected_type_name)

    @pytest.mark.parametrize(
        "price, expected_type_price",
        [
            (988.0, float),
            (1255.0, float),
        ],
    )
    def test_price_type(self, price, expected_type_price):
        bun = Bun("Флюоресцентная булка R2-D3", price)
        assert isinstance(bun.get_price(), expected_type_price)
