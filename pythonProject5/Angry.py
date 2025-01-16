from Mood import Mood

class Angry(Mood):
    def __init__(self, strength=2):
        self.__strength = strength

    def get_strength(self):
        return self.__strength

    def get_patience_factor(self, waiting_time):
        Factor = round((1.3 ** (waiting_time/5)) * self.get_strength(), 2)
        return Factor

    def __repr__(self):
        return "Angry"
