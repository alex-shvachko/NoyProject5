class NoSuchIngredientException(Exception):
    def __init__(self, ingredient):
        super().__init__()
        self.ingredient = ingredient
    def __str__(self):
        return f"Error:\n”{self.ingredient}” is an invalid ingredient."

class NotCustomerDishException(Exception):
    def __init__(self,suggested_dish, expected_dish):
        super().__init__()
        self.suggested_dish = suggested_dish
        self.expected_dish = expected_dish
    def __str__(self):
        return f"Error:\nThe suggested dish:\t{self.suggested_dish}\nis not as expected:\t{self.expected_dish}."

class NoSuchOrderException(Exception):
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__()
    def __str__(self):
        return f"Error:\nOrderID: “{self.order_id}” does not exist."

class OrderOutOfBoundsException(Exception):
    pass