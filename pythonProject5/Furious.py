from Angry import Angry
from Mood import Mood

class Furious(Angry):
    def __init__(self, strength=2):
        super().__init__(strength)
        self.__strength = strength

    def get_strength(self):
        return self.__strength

    def get_patience_factor(self, waiting_time):
        new_factor = round(super().get_patience_factor(waiting_time) * 1.5, 2)
        return new_factor

    def __eq__(self, other):
        if not isinstance(other, Furious):
            return False
        return self.get_strength() == other.get_strength()

    def __repr__(self):
        return "Furious"

