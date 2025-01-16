from unittest import TestCase
from Calm import Calm

class test_Calm(TestCase):
    def test_get_patience_factor_custom_strength(self):
        calm = Calm(strength=3)
        expected_factor = round(1.05 ** (5 / 5) * 3, 2)
        self.assertEqual(calm.get_patience_factor(5), expected_factor)

    def test_get_patience_factor_large_waiting_time(self):
        calm = Calm(strength=2)
        expected_factor = round(1.05 ** (10 / 5) * 2, 2)
        self.assertEqual(calm.get_patience_factor(10), expected_factor)

    def test_repr(self):
        calm = Calm(strength=2)
        self.assertEqual(repr(calm), "Calm")

