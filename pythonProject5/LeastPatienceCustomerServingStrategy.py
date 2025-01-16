from ServingStrategy import ServingStrategy
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException


class LeastPatienceCustomerServingStrategy(ServingStrategy):
    def select_next_order(self, orders):
        least_p = None
        if not orders:
            raise OrderOutOfBoundsException

        if not orders:
            raise OrderOutOfBoundsException
        least_p = None
        for order_id in orders:
            customer, dish = orders[order_id]
            if least_p is None or customer.get_patience() < orders[least_p][0].get_patience():
                least_p = order_id
        return least_p

        # least_p = sorted(orders.items(), key=lambda item: (item[1][0].get_patience(), item[0]))
        # return least_p[0]
