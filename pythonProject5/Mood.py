from abc import ABC, abstractmethod

class Mood(ABC):
    @abstractmethod
    def get_patience_factor(self, waiting_time):
        Factor = round((1.3 ** (waiting_time / 5)) * self.get_strength(), 2)
        return Factor
