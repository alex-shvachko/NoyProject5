from Mood import Mood

class Chill(Mood):
    def __init__(self, strength=2, chill_modifier=0.5):
        self.__strength = strength
        self.__chill_modifier = chill_modifier

    def get_strength(self):
        return self.__strength

    def get_chill_modifier(self):
        return self.__chill_modifier

    def get_patience_factor(self, waiting_time):
        Factor = round((1.05 ** (waiting_time / 5)) * self.get_strength() * self.get_chill_modifier(), 2)
        return Factor

    def __repr__(self):
        return "Chill"