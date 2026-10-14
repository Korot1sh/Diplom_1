import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.fixture
    def ingredient(self):
        return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

    def test_get_price_returns_ingredient_price(self, ingredient):
        assert ingredient.get_price() == 50

    def test_get_name_returns_ingredient_name(self, ingredient):
        assert ingredient.get_name() == "hot sauce"

    @pytest.mark.parametrize(
        "ingredient_type",
        [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "ingredient", 100)

        assert ingredient.get_type() == ingredient_type
