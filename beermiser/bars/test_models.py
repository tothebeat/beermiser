from django.test import TestCase

from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

from .models import Bar, Beer

class BarTestModel(TestCase):
    """
    Class to test the model
    Bar
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.bar = mommy.make(Bar)


class BeerTestModel(TestCase):
    """
    Class to test the model
    Beer
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.beer = mommy.make(Beer)
