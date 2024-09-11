import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_name",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0, "Соус традиционный галактический"),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0, "Мясо бессмертных моллюсков"),
            (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80.0, "Соус фирменный Space Sauce"),
        ],
    )
    def test_get_name(self, ingredient_type, name, price, expected_name):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name, "Имя ингредиента неверное"

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0, 15.0),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0, 1337.0),
            (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80.0, 80.0),
        ],
    )
    def test_get_price(self, ingredient_type, name, price, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price, "Цена ингредиента неверная"

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0, INGREDIENT_TYPE_FILLING),
        ],
    )
    def test_get_type(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type, "Тип ингредиента неверный"

    @pytest.mark.parametrize(
        "initial_name, new_name",
        [
            ("Соус Spicy-X", "Соус Межгалактический"),
            ("Соус Galaxy", "Соус Интергалактический"),
        ],
    )
    def test_change_name_with_mock(self, initial_name, new_name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, initial_name, 90.0)
        ingredient.get_name = Mock(return_value=new_name)
        assert ingredient.get_name() == new_name
        ingredient.get_name.assert_called_once()

    @pytest.mark.parametrize(
        "initial_price, new_price",
        [
            (1337.0, 1000.0),
            (200.0, 150.0),
        ],
    )
    def test_change_price_with_mock(self, initial_price, new_price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", initial_price)
        ingredient.get_price = Mock(return_value=new_price)
        assert ingredient.get_price() == new_price
        ingredient.get_price.assert_called_once()

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0),
        ],
    )
    def test_name_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.get_name(), str), "Тип имени должен быть строкой"

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0),
        ],
    )
    def test_price_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.get_price(), float), "Тип цены должен быть float"

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0),
        ],
    )
    def test_type_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.get_type(), str), "Тип значения должен быть строкой"

    def test_valid_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0)
        assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING], "Тип ингредиента недопустимый"
