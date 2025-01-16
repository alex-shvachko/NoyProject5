from Mood import Mood

class Explosive(Mood):
    def __init__(self, strength=2):
        self.__strength = strength

    def get_strength(self):
        return self.__strength

    def get_patience_factor(self, waiting_time):
        Factor = round(1.3 ** ((waiting_time *  self.get_strength())/ 5), 2)
        return Factor

    def __repr__(self):
        return "Explosive"

