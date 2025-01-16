from unittest import TestCase
from TypeA import TypeA
from Calm import Calm
from Explosive import Explosive
from Furious import Furious
from Angry import Angry

class test_TypeA(TestCase):
    def test_adjust_mood_explosive(self):
        type_a = TypeA()
        initial_mood = Calm()  # Assume Calm is a valid Mood subclass
        adjusted_mood = type_a.adjust_mood(initial_mood, 41)  # 41 seconds should result in Explosive mood
        self.assertIsInstance(adjusted_mood, Explosive)

    def test_adjust_mood_furious(self):
        type_a = TypeA()
        initial_mood = Calm()  # Assume Calm is a valid Mood subclass
        adjusted_mood = type_a.adjust_mood(initial_mood, 35)  # 35 seconds should result in Furious mood
        self.assertIsInstance(adjusted_mood, Furious)

    def test_adjust_mood_angry(self):
        type_a = TypeA()
        initial_mood = Calm()  # Assume Calm is a valid Mood subclass
        adjusted_mood = type_a.adjust_mood(initial_mood, 25)  # 25 seconds should result in Angry mood
        self.assertIsInstance(adjusted_mood, Angry)