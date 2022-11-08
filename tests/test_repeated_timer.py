from unittest import TestCase
from unittest.mock import patch
from src.repeated_timer import RepeatedTimer
import time

class TestRepeatedTimer(TestCase):
    def test_can_create_class(self):
        actual_timer = RepeatedTimer(10, print)
        self.assertEqual(actual_timer.interval, 10)
        self.assertEqual(actual_timer.function, print)
        actual_timer.stop()

    def test_create_class_starts(self):
        actual_timer = RepeatedTimer(10, print)
        self.assertEqual(actual_timer.is_running, True)
        actual_timer.stop()

    def test_Can_stop_timer(self):
        actual_timer = RepeatedTimer(10, print)
        # confirm its running
        self.assertEqual(actual_timer.is_running, True)
        actual_timer.stop()
        self.assertEqual(actual_timer.is_running, False)

    def test_can_update_interval(self):
        actual_timer = RepeatedTimer(10, print)
        # confirm the interval is 10
        self.assertEqual(actual_timer.interval, 10)
        actual_timer.updateInterval(100)
        self.assertEqual(actual_timer.interval, 100)
        self.assertEqual(actual_timer.is_running, True)
        actual_timer.stop()

    def test_can_start_when_stopped(self):
        actual_timer = RepeatedTimer(10, print)
        actual_timer.stop()
        self.assertEqual(actual_timer.is_running, False)
        actual_timer.start()
        self.assertEqual(actual_timer.is_running, True)
        actual_timer.stop()

    def test_cannot_start_when_running(self):
        actual_timer = RepeatedTimer(60, print)
        self.assertEqual(actual_timer.is_running, True)
        current_time = time.time()
        actual_timer.start()
        self.assertNotEqual(actual_timer.next_call, current_time + 60)
        actual_timer.stop()

    @patch('builtins.print')
    def test_timer_checks_correct_times(self, print):
        start_time = time.time()
        actual_timer = RepeatedTimer(2, print)
        while (start_time + 10 > time.time()):
            i = 1
        actual_timer.stop()
        self.assertEqual(print.call_count, 5)