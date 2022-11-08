import unittest
import src.analysis as analytics


class TestAnalytics(unittest.TestCase):
    def test_time_message(self):
        data = {'chain': 'Crystalvale', 'time': 1666921395, 'working': False, 'awayUntil': 1667519273, 'workingUntil': 1666858528}
        previousData = {'chain': 'Crystalvale', 'time': 1666921395, 'working': False, 'awayUntil': 1667519273, 'workingUntil': 1666858528}
        response = analytics.extractData(data, previousData)
        print(response)
