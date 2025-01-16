import time
from Dish import Dish
from FalafelStall import FalafelStall
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException
from Customer import Customer
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.__orders_strategy = orders_strategy
        self.__serving_strategy = serving_strategy
        self.__ingredient_prices = ingredient_prices
        self.game_start = int(time.time())
        self.lives = 3
        self.__ingredient_dictionary = self.__create_ingredient_dictionary(ingredient_prices)

    def __create_ingredient_dictionary(self, ingredient_prices):
        ingredient_dictionary ={}
        i=0
        for ingredient, price in ingredient_prices.items():

            ingredient_dictionary[i] = ingredient
            i+=1
        return ingredient_dictionary

    def get_lives(self):
        return self.lives

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.game_start

    def create_dish(self, user_num):
        user_num_str = user_num.split()
        ingredients = []
        for index in user_num_str:
            if index.isdigit():
                index=int(index)
                if 0 <= index <= len(self.__ingredient_dictionary.keys())-1:
                    ingredients.append((self.__ingredient_dictionary[index]))
            else:
                ingredients.append("")

            if "" in ingredients:
                raise NoSuchIngredientException("")
        return Dish(ingredients)

    def update_mood_customer(self, falafel_stall):
        removed_orders = []
        for order_id in falafel_stall.get_orders().keys():
            falafel_stall.get_orders()[order_id][0].update(falafel_stall.get_orders()[order_id][0].get_waiting_time())
            if falafel_stall.get_orders()[order_id][0].get_patience <= 0:
                removed_orders.append(order_id)
                self.lives = self.lives-1
            if self.lives <= 0:
                print(f"Game Over\nscore: {falafel_stall.get_earning()}")
                return -1
        for del_orders in removed_orders:
            falafel_stall.remove_order(del_orders)

    def create_orders(self, falafel_stall):
        orders = next(self.__orders_strategy)
        order_ids = []
        for order in orders:
            customer = order[0]
            wanted_dish = order[1]
            order_id = falafel_stall.get_order(customer,wanted_dish)
            order_ids.append((customer, wanted_dish))
        return order_ids

    def orders_by_strategy(self, falafel_stall):
        orders = falafel_stall.get_orders
        sorted_orders = self.__serving_strategy(orders)
        for order_id, (customer, ordered_dish) in sorted_orders:
            print(f"Customer:\n{customer}\nDish: {ordered_dish}")

    def run(self):
        falafel_stall = FalafelStall(self.__serving_strategy, self.__ingredient_prices)
        while True:
            orders = next(self.__orders_strategy)
            if orders:
                for customer, ordered_dish in orders:
                    falafel_stall.order(customer, ordered_dish)
            self.orders_by_strategy(falafel_stall)
            for order_id, (customer, ordered_dish) in falafel_stall.get_orders().items():
            #     #order_id = falafel_stall.order(customer, ordered_dish)
                 print(f"Customer:\n{customer}\nDish: {ordered_dish}")
            # #curr_id = self.__serving_strategy.


            print("Insert ingredients:")
            for index, ingredient in self.__ingredient_dictionary.items():
                print(f"{index}: {ingredient}")


            user_num = input()
            try:
                new_dish = self.create_dish(user_num)
                falafel_stall.serve_dish(order_id, new_dish)
            except NoSuchIngredientException as e:
                print(f"Failed to create a Dish\n{e}\nplease retry.")
            except (NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException) as e:
                print(f"Failed to serve a Dish to customer\n{e}")
                #continue

                    #continue
            # except StopIteration:
            #      break
            finish = self.update_mood_customer(falafel_stall)
            if finish == -1:
                break
        print(f"Game Over\nscore: {falafel_stall.get_earning()}")
        # for order_id, (customer, _) in list(falafel_stall.get_orders().items()):
            #     customer.get_mood(-1)
            #     if customer.get_mood() <= 0:
            #         falafel_stall.remove_order(order_id)


        #             self.lives -= 1
        #     if not falafel_stall.get_orders():
        #         break
        # print(f"Game Over\nscore: {falafel_stall.get_earning()}")


