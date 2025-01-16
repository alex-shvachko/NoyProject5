class Dish:
    def __init__(self, ingredients=None):
        self.__ingredients = ingredients if ingredients else []

    def get_ingredients(self):
        return self.__ingredients

    def add_ingredient(self, ingredient):
        return self.get_ingredients().append(ingredient)

    def __eq__(self, other):
        if not isinstance(other, Dish):
            return False
        return len(self.get_ingredients()) == len(other.get_ingredients()) and all(ingredient in other.get_ingredients() for ingredient in self.get_ingredients())

    def __repr__(self):
        return "* " + ", ".join(self.__ingredients) + " *"
