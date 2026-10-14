from unittest.mock import Mock

import pytest

from burger import Burger


class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def bun(self):
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        return bun

    @pytest.fixture
    def ingredient(self):
        ingredient = Mock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 50
        return ingredient

    def test_set_buns_sets_bun(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_moves_ingredient(self, burger):
        first = Mock()
        second = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [second, first]

    def test_get_price_returns_total_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 250

    def test_get_receipt_returns_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_receipt() == (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 250"
        )
