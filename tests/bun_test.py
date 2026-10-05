import pytest
from bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 200),
    ],
)
def test_get_name_returns_bun_name(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
