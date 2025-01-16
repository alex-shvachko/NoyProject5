import time

#from sympy import false

from Dish import Dish
from FalafelStall import FalafelStall
from exceptions import NoSuchIngredientException, NotCustomerDishException, OrderOutOfBoundsException


class Game:
    def __init__(self,orders_strategy,serving_strategy,ingredient_prices):
        self.__orders_strategy = orders_strategy
        self.__serving_strategy = serving_strategy
        self.__ingredient_prices = ingredient_prices
        self.__game_start = float(time.time())
        self.__lives = 3
        self.__ingredient_dictionary = {}

    def get_lives(self):
        return self.__lives

    def get_game_duration(self,current_time=None):
        if current_time is None:
            current_time = float(time.time())
        return current_time - self.__game_start

    def __create_ingredient_dict(self):
        counter = 0
        # creating the ingredients dictionary
        for ing in self.__ingredient_prices.keys():
            self.__ingredient_dictionary[counter] = ing
            counter += 1

    def __create_orders_dict(self,falafel):
            # creating a list of orders
            try:
                orders = next(self.__orders_strategy)
            except StopIteration:
                if not falafel.get_orders():
                    print(f"Game Over")
                    print(f"score: {float(falafel.get_earning())}")
                    return
                else:
                    return []
                # putting all the orders in a dictionary
            for order in orders:
                customer = order[0]
                expected_dish = order[1]
                falafel.order(customer, expected_dish)

    def __print_ingredients(self):
        # printing the ingredients
        for key, val in self.__ingredient_dictionary.items():
            print(f"{key}: {val}")

    def __check_dish(self):
        # typing the dish and turning it into a list
        made_dish = Dish()
        dish_numbers = input("")
        dish_numbers_lst = dish_numbers.split(" ")

        # checking if all the represent an ingredient
        check = 0
        while check < len(dish_numbers_lst):
            try:
                if int(dish_numbers_lst[check]) in self.__ingredient_dictionary.keys():
                    made_dish.add_ingredient(self.__ingredient_dictionary[int(dish_numbers_lst[check])])
                    check += 1
                else:
                    print(f"Failed to create a dish")
                    raise NoSuchIngredientException(dish_numbers[check])
            except NoSuchIngredientException as e:
                print(f"{e}\nplease retry.")
                made_dish = Dish()
                dish_numbers = input()
                dish_numbers_lst = dish_numbers.split(" ")
                check = 0
        return made_dish

    def __update_mood_patience(self,falafel):
        delete_keys = []
        for key, order in falafel.get_orders().items():
            order[0].update(order[0].get_waiting_time())
            if order[0].get_patience() <= 0:
                self.__lives = self.__lives - 1
                delete_keys.append(key)
                if self.__lives <= 0:
                    print(f"Game Over")
                    print(f"score: {float(falafel.get_earning())}")
                    return -1
        for key in delete_keys:
            falafel.remove_order(key)


    def run(self):
        self.__create_ingredient_dict()
        falafel = FalafelStall(self.__serving_strategy, self.__ingredient_prices)
        while True:
            self.__create_orders_dict(falafel)

            try:
                order_id = falafel.get_next_order_id()
                current_order = falafel.get_orders()[order_id]
                current_customer = current_order[0]
                current_dish = current_order[1]
                print(f"Customer:\n{current_customer}\nDish: {current_dish}")
                print("Insert ingredients:")
            except OrderOutOfBoundsException:
                return
            self.__print_ingredients()

            made_dish = self.__check_dish()

            #if the dish is correct then updating the dictionary
            try:
                if made_dish == current_dish:
                    falafel.serve_dish(order_id, made_dish)
                    falafel.remove_order(order_id)
                else:
                    raise NotCustomerDishException(made_dish,current_dish)
            except NotCustomerDishException as e:
                print(f"Failed to serve a Dish to customer\n{e}")
                #updating the mood patience and lives accordingly
            game_over = self.__update_mood_patience(falafel)
            if game_over == -1:
                return






