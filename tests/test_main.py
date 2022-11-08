from unittest import TestCase
from unittest.mock import patch


class Test(TestCase):
    def test_true_assertions(self):
        self.assertTrue(True)