from unittest.mock import Mock
from burger import Burger


def test_set_buns_sets_bun():
    burger = Burger()
    bun = Mock()

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_adds_ingredient():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_get_price_returns_total_price():
    burger = Burger()
    bun = Mock()
    bun.get_price.return_value = 100
    ingredient = Mock()
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    price = burger.get_price()

    assert price == 250


def test_get_receipt_returns_receipt():
    burger = Burger()
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert receipt == (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 250"
    )