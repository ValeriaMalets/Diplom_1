import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price, expected_name, expected_price",
        [
            ("Флюоресцентная булка R2-D3", 988.0, "Флюоресцентная булка R2-D3", 988.0),
            ("Краторная булка N-200i", 1255.0, "Краторная булка N-200i", 1255.0)
        ],
    )
    def test_get_name_and_price(self, name, price, expected_name, expected_price):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_change_name_with_mock(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988.0)
        new_name = "Солнечная булка"

        bun.get_name = Mock(return_value=new_name)

        assert bun.get_name() == new_name
        bun.get_name.assert_called_once()

    def test_change_price_with_mock(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988.0)
        new_price = 1000.0

        bun.get_price = Mock(return_value=new_price)

        assert bun.get_price() == new_price
        bun.get_price.assert_called_once()

    @pytest.mark.parametrize(
        "name, price, expected_type_name, expected_type_price",
        [
            ("Флюоресцентная булка R2-D3", 988.0, str, float),
            ("Краторная булка N-200i", 1255.0, str, float),
        ],
    )
    def test_types(self, name, price, expected_type_name, expected_type_price):
        bun = Bun(name, price)
        assert isinstance(bun.get_name(), expected_type_name)
        assert isinstance(bun.get_price(), expected_type_price)
