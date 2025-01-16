from abc import ABC, abstractmethod

class Mood(ABC):
    @abstractmethod
    def get_patience_factor(self, waiting_time):
        pass
