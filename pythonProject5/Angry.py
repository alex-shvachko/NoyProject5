from Mood import Mood

class Angry(Mood):
    def __init__(self, strength=2):
        self.__strength = strength

    def get_strength(self):
        return self.__strength

    def __eq__(self, other):
        if not isinstance(other, Angry):
            return False
        return self.get_strength() == other.get_strength()

    def get_patience_factor(self, waiting_time):
        Factor = round((1.1 ** (waiting_time / 10)) * self.get_strength(), 2)
        return Factor

    def __repr__(self):
        return "Angry"
