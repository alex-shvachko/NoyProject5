from abc import ABC, abstractmethod
class ServingStrategy(ABC):
    @abstractmethod
    def select_next_order(self, orders):
        pass
