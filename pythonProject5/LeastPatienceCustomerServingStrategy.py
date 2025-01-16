from ServingStrategy import ServingStrategy
from exceptions import NoSuchIngredientException, NoSuchOrderException, OrderOutOfBoundsException, NotCustomerDishException


class LeastPatienceCustomerServingStrategy(ServingStrategy):
    def select_next_order(self, orders):
        if not orders:
            return None
        min_patience = float('inf')
        selected_order = None
        for order_id, (customer, dish) in orders.items():
            patience = customer.get_patience()
            if patience < min_patience or (patience == min_patience and order_id < (selected_order or float('inf'))):
                min_patience = patience
                selected_order = order_id
        return selected_order