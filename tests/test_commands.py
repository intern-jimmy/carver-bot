from unittest import TestCase
from src.commands import Commands

class TestCommands(TestCase):
    def test_Commands_quit_value(self):
        self.assertEqual(Commands.QUIT.value, 1)

    def test_Commands_help_value(self):
        self.assertEqual(Commands.HELP.value, 2)

    def test_Commands_debug_value(self):
        self.assertEqual(Commands.DEBUG.value, 3)

    def test_Commands_interval_value(self):
        self.assertEqual(Commands.INTERVAL.value, 4)

    def test_Commands_status_value(self):
        self.assertEqual(Commands.STATUS.value, 5)