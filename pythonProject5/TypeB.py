from Personality import Personality
from Furious import Furious
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Explosive import Explosive

class TypeB(Personality):
    def adjust_mood(self, mood, waiting_time):
        if isinstance(mood, Furious) and waiting_time > 120:
            return Explosive()
        elif isinstance(mood, Angry) and waiting_time > 90:
            return Furious()
        elif isinstance(mood, Calm) and waiting_time > 60:
            return Angry()
        elif isinstance(mood, Chill) and waiting_time > 40:
            return Calm()
        return mood

    def __repr__(self):
        return "TypeB"

    def __eq__(self, other):
        if not isinstance(other, TypeB):
            return False
        return True
