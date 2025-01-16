import random
from OrdersStrategy import OrdersStrategy
from Customer import Customer
from Dish import Dish
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Furious import Furious
from TypeA import TypeA
from TypeB import TypeB

class RandomOrdersStrategy(OrdersStrategy):
    def __init__(self, max_dishes, max_ingredients, ingredients, n_orders=-1):
        self.max_ingredients = max_ingredients
        self.__ingredients = ingredients
        self.__n_orders = n_orders
        self.current = 0
        self.max_dishes = max_dishes
    def get_ingredients(self):
        return self.__ingredients

    def get_n_orders(self):
        return self.__n_orders

    def __iter__(self):
        return self

    def __next__(self):
        if self.get_n_orders() != -1 and self.current >= self.get_n_orders():
            raise StopIteration
        num_dishes = random.randint(0, self.max_dishes)
        orders =[]
        for _ in range(num_dishes):
            self.current += 1
            unique_name = f"{self.current}"
            mood = random.choice([Angry(), Calm(), Chill(), Furious()])
            personality = random.choice([TypeA(), TypeB()])
            customer = Customer(unique_name, mood, personality)
            num_ingredients = random.randint(1,self.max_ingredients)
            dish_ingredients = random.sample(self.get_ingredients(), num_ingredients)
            dish = Dish(dish_ingredients)
            orders.append((customer, dish))
        return orders
