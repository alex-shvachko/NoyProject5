from ServingStrategy import ServingStrategy
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException

class ArrivalTimeServingStrategy(ServingStrategy):
    def select_next_order(self, orders):
        #earliest_order = None
        if not orders:
            raise OrderOutOfBoundsException
        earliest_order = None
        for order_id in orders:
            customer, dish = orders[order_id]
            if earliest_order is None or customer.get_arrive_time() < orders[earliest_order][0].arrive_time:
                earliest_order = order_id
        return earliest_order

        # earliest_order = sorted(orders.items(), key=lambda item: (item[1][0].get_arrive_time(), item[0]))
        # return earliest_order[0]