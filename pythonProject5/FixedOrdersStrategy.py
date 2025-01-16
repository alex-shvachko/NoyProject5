from OrdersStrategy import OrdersStrategy

class FixedOrdersStrategy(OrdersStrategy):
    def __init__(self, lst_orders):
        self.__lst_orders = lst_orders
        self.index = 0

    def get_lst_orders(self):
        return self.__lst_orders

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.get_lst_orders()):
            raise StopIteration
        order = self.get_lst_orders()[self.index]
        self.index += 1
        return order