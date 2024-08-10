from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_available_buns_list_not_empty(self):
        database = Database()
        assert len(database.available_buns()) > 0

    def test_available_ingredients_list_not_empty(self):
        database = Database()
        assert len(database.available_ingredients()) > 0

    def test_available_buns_contains_bun_objects(self):
        database = Database()
        buns = database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_contains_ingredient_objects(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    def test_buns_and_ingredients_initialization(self):
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
