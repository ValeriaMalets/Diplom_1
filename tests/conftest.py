import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Краторная булка N-200i"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient1():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Мясо бессмертных моллюсков"
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_price.return_value = 50
    return ingredient


@pytest.fixture
def mock_ingredient2():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Соус Spicy-X"
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_price.return_value = 30
    return ingredient


@pytest.fixture
def burger(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger
