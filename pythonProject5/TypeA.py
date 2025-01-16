from Personality import Personality
from Explosive import Explosive
from Furious import Furious
from Angry import Angry
class TypeA(Personality):
    def adjust_mood(self, mood, waiting_time):
        if waiting_time > 40:
            return Explosive()
        elif waiting_time > 30:
            return Furious()
        elif waiting_time > 20:
            return Angry()
        return mood

    def __repr__(self):
        return "TypeA"





