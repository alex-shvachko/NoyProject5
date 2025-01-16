from abc import ABC, abstractmethod

class Personality(ABC):
    @abstractmethod
    def adjust_mood(self, mood, waiting_time):
        pass