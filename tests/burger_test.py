class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient1

    def test_add_multiple_ingredients(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        assert len(burger.ingredients) == 2
        assert burger.ingredients == [mock_ingredient1, mock_ingredient2]

    def test_remove_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    def test_get_price(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        assert burger.get_price() == 250

    def test_get_price_multiple_ingredients(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        assert burger.get_price() == 280

    def test_get_receipt(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = (
            "(==== Краторная булка N-200i ====)\n"
            "= filling Мясо бессмертных моллюсков =\n"
            "= sauce Соус Spicy-X =\n"
            "(==== Краторная булка N-200i ====)\n"
            "Price: 280"
        )

        assert burger.get_receipt() == expected_receipt
