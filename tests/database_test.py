from database import Database


def test_available_buns_returns_buns():
    database = Database()

    buns = database.available_buns()

    assert len(buns) == 3


def test_available_ingredients_returns_ingredients():
    database = Database()

    ingredients = database.available_ingredients()

    assert len(ingredients) == 6