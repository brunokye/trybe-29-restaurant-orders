import pytest
from src.models.dish import Dish
from src.models.ingredient import Restriction, Ingredient


# Req 2
def test_dish():
    panqueca_01 = Dish('panqueca', 5.99)
    panqueca_02 = Dish('panqueca', 5.99)
    misto = Dish('misto', 2.99)

    ovo = Ingredient('ovo')

    name_test, price_test = panqueca_01.name, panqueca_01.price
    assert panqueca_01.__repr__() == f"Dish('{name_test}', R${price_test})"

    assert panqueca_01.__eq__(panqueca_02) is True
    assert panqueca_01.__eq__(misto) is False

    assert panqueca_01.__hash__() == panqueca_02.__hash__()
    assert panqueca_01.__hash__() != misto.__hash__()

    panqueca_01.add_ingredient_dependency(ovo, 2)
    assert panqueca_01.get_restrictions() == {Restriction.ANIMAL_DERIVED}
    assert panqueca_01.get_ingredients() == {Ingredient('ovo')}

    with pytest.raises(TypeError):
        Dish('lasanha', '1')

    with pytest.raises(ValueError):
        Dish('pizza', -2)
