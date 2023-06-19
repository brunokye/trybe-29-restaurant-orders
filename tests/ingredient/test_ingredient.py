from src.models.ingredient import Restriction, Ingredient


# Req 1
def test_ingredient():
    tomate_01 = Ingredient('tomate')
    tomate_02 = Ingredient('tomate')
    farinha = Ingredient('farinha')

    assert farinha.restrictions == {Restriction.GLUTEN}

    assert tomate_01.__hash__() == tomate_02.__hash__()
    assert tomate_01.__hash__() != farinha.__hash__()

    assert tomate_01.__eq__(tomate_02) is True
    assert tomate_01.__eq__(farinha) is False

    name_test = farinha.name
    assert farinha.__repr__() == f"Ingredient('{name_test}')"
