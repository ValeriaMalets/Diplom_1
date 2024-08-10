import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_name, expected_price, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0, "Соус традиционный галактический", 15.0,
             INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0, "Мясо бессмертных моллюсков", 1337.0,
             INGREDIENT_TYPE_FILLING),
            (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80.0, "Соус фирменный Space Sauce", 80.0,
             INGREDIENT_TYPE_SAUCE),
        ],
    )
    def test_ingredient_attributes(self, ingredient_type, name, price, expected_name, expected_price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
        assert ingredient.get_type() == expected_type

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
        "ingredient_type, name, price, expected_type_name, expected_type_price, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0, str, float, str),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков", 1337.0, str, float, str),
        ],
    )
    def test_types(self, ingredient_type, name, price, expected_type_name, expected_type_price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.get_name(), expected_type_name)
        assert isinstance(ingredient.get_price(), expected_type_price)
        assert isinstance(ingredient.get_type(), expected_type)

    def test_valid_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0)
        assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
