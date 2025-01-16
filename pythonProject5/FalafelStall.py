from os.path import split

from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException


class FalafelStall:
    def __init__(self, strategy, ingredient_prices):
        self.__strategy = strategy
        self.__ingredient_prices = ingredient_prices
        self.orders = {}
        self.money = 0
        self.order_counter = 1

    def get_strategy(self):
        return self.__strategy

    def get_ingredient_prices(self):
        return self.__ingredient_prices

    def order(self, customer, dish):
        order_id = self.order_counter
        for ingredient in dish.get_ingredients():
            if ingredient not in self.__ingredient_prices:
                raise NoSuchIngredientException
        self.orders[order_id] = (customer, dish)
        self.order_counter += 1
        return order_id

    def get_next_order_id(self):
        if not self.orders:
            raise OrderOutOfBoundsException
        return self.get_strategy().select_next_order(self.orders)

    def serve_dish(self, order_id, dish):
        if order_id not in self.orders.keys():
             raise NoSuchOrderException
        if not isinstance(order_id, int):
            raise TypeError
        # if order_id not in self.orders.keys():
        #     raise NoSuchOrderException
        try:
            order_dish = self.orders[order_id][1]
            # customer, order_dish = self.orders[order_id]
            if order_dish == dish:
                for ingredient in dish.get_ingredients():
                    if ingredient in self.get_ingredient_prices().keys():
                        self.money += self.calculate_cost(dish)
                self.remove_order(order_id)
            else:
                raise NotCustomerDishException(order_dish,dish)
        except NotCustomerDishException as e:
            print(f"Failed to serve a Dish to customer\n{e}")

            # self.money += self.calculate_cost(dish)
        # del self.orders[order_id]
        # return True
        # if not isinstance(order_id, int):
        #     raise TypeError
        # if order_id not in self.orders.keys():
        #     raise NoSuchOrderException
        # for order_ids in self.orders.items():
        #     if order_ids[1] == dish:
        #         ingredients_str = split(order_ids[1])
        #         for ingredient in self.get_ingredient_prices().keys():
        #             for ing in ingredients_str:
        # #                 if ing == ingredient:
        # #                     self.money += self.calculate_cost(dish)
        # self.remove_order(order_id)
        # return True

    def remove_order(self, order_id):
        if order_id not in self.orders:
            raise NoSuchOrderException
        else:
            del self.orders[order_id]

    def get_order(self, order_id):
        if order_id not in self.orders.keys():
            raise NoSuchOrderException
        return self.orders[order_id]

    def calculate_cost(self, dish):
        total_cost = 0
        for ingredient in dish.get_ingredients():
            if ingredient not in self.__ingredient_prices:
                raise NoSuchIngredientException
            total_cost += self.__ingredient_prices[ingredient]
        return total_cost

    def get_orders(self):
        return self.orders

    def get_earning(self):
        return self.money