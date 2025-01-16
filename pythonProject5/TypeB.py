from Personality import Personality
from Furious import Furious
from Angry import Angry
from Calm import Calm
from Chill import Chill
from Explosive import Explosive

class TypeB(Personality):
    def adjust_mood(self, mood, waiting_time):
        if waiting_time > 120 and mood == Furious():
            return Explosive()
        elif waiting_time > 90 and mood == Angry():
            return Furious()
        elif waiting_time > 60 and mood == Calm():
            return Angry()
        elif waiting_time > 40 and mood == Chill():
            return Calm()
        return mood

    def __repr__(self):
        return "TypeB"


