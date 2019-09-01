from django.test import TestCase

from app.calc import add, subtract

class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8), 11)

    def test_sub_numbers(self):
        """ Test that two numbers are subtracted together"""
        self.assertEquals(subtract(5,11),6)
