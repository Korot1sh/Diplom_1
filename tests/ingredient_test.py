import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    "ingredient_type",
    [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
)
def test_get_type_returns_ingredient_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, "ingredient", 100)

    assert ingredient.get_type() == ingredient_type