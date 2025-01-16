from ServingStrategy import ServingStrategy
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException


class LongestWaitingTimeServingStrategy(ServingStrategy):
    def select_next_order(self, orders):
        longest = None
        if not orders:
            raise OrderOutOfBoundsException

        if not orders:
            raise OrderOutOfBoundsException
        longest = None
        for order_id in orders:
            customer, dish = orders[order_id]
            if longest is None or customer.get_waiting_time() > orders[longest][0].get_waiting_time():
                longest = order_id
        return longest

        # longest = sorted(orders.items(), key=lambda item: (item[1][0].get_waiting_time(), item[0], -1))
        # return longest[0]
