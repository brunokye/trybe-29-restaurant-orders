import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set(self._process_menu_data(source_path))

    def _process_menu_data(self, source_path: str):
        with open(source_path, newline='') as file:
            lines = csv.DictReader(file)
            dishes = set()

            for data in lines:
                name = data['dish']
                price = float(data['price'])
                ingredient = data['ingredient']
                recipe_amount = int(data['recipe_amount'])

                dishes.add(Dish(name, price))

                current_dish = next(iter(dishes))

                current_dish.add_ingredient_dependency(
                    Ingredient(ingredient), recipe_amount
                )

            return dishes
