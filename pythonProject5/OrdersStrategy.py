from abc import ABC, abstractmethod
class OrdersStrategy(ABC):
    @abstractmethod
    def __next__(self):
        pass
