import unittest

from Dish import Dish
from unittest import TestCase
class test_Dish(TestCase):
    def test_add_ingredient(self):
        dish = Dish(['falafel'])
        dish.add_ingredient('humus')
        self.assertEqual(dish.get_ingredients(), ['falafel', 'humus'])

    def test_eq_equal_dishes(self):
        dish1 = Dish(['falafel', 'humus'])
        dish2 = Dish(['humus', 'falafel'])
        self.assertTrue(dish1 == dish2)

    def test_repr(self):
        dish = Dish(['falafel', 'humus', 'french fries'])
        self.assertEqual(repr(dish), "* falafel, humus, french fries *")
