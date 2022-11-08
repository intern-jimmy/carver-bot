import unittest
from src.messages import create_message


class MyTestCase(unittest.TestCase):
    def test_create_message_status_changed_now_working(self):
        """ Working status changed and he is now working """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 1,
            "seconds": 1,
            "working": True,
            "workingStatusChanged": True,
            "timeLeft": 6458
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '🚨  The Stone Carver has arrived in internville! 🚨\n\nGet those stones quick, before he ' \
                           'heads out on the road again in 1 day 1 hour 1 minute 1 second \n\n#DeFiKingdoms'

        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['interval'], 600)

    def test_create_message_status_changed_not_working(self):
        """ Working status changed and he is not working """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 1,
            "seconds": 1,
            "working": False,
            "workingStatusChanged": True,
            "timeLeft": 6458
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = 'He Gone! 🏃‍♂️💨\n\nThe Stone Carver has left! He will be back to internville in 1 day 1 ' \
                           'hour 1 minute 1 second !\n\n #DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['oneHourMessage'], False)
        self.assertEqual(actual_response['interval'], 600)

    def test_create_message_working_no_status_change_61_minutes(self):
        """ Working and minutes >"""
        data = {
            "days": 0,
            "hours": 0,
            "minutes": 61,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 61 * 60
        }
        one_hour_sent = False
        realm = "internville"
        expected_message = ''
        interval_time = 600
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_1_hour_1_minutes(self):
        """ Working and hour and minutes >"""
        data = {
            "days": 0,
            "hours": 1,
            "minutes": 1,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 61 * 60
        }
        one_hour_sent = False
        realm = "internville"
        expected_message = ''
        interval_time = 600
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_60_minutes(self):
        """ Working and time is exact minutes """
        data = {
            "days": 0,
            "hours": 0,
            "minutes": 60,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '⏰  One hour left before the Stone Carver leaves! ⏰\n\n#DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_59_minutes(self):
        """ Working and minutes is < and message not sent """
        data = {
            "days": 0,
            "hours": 0,
            "minutes": 59,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 59 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '⏰  One hour left before the Stone Carver leaves! ⏰\n\n#DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_1_hour(self):
        """ Working and hours are exact """
        data = {
            "days": 0,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '⏰  One hour left before the Stone Carver leaves! ⏰\n\n#DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_60_minutes_already_sent(self):
        """ Working and time is exact minutes """
        data = {
            "days": 0,
            "hours": 0,
            "minutes": 60,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = True
        realm = "internville"
        expected_message = ''
        interval_time = 600
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_59_minutes_already_sent(self):
        """ Working and minutes is < and message not sent """
        data = {
            "days": 0,
            "hours": 0,
            "minutes": 59,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 59 * 60
        }
        one_hour_sent = True
        realm = "internville"
        expected_message = ''
        interval_time = 600
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_1_hour_already_sent(self):
        """ Working and hours are exact """
        data = {
            "days": 0,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = True
        realm = "internville"
        expected_message = ''
        interval_time = 600
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_1_day_60_minutes(self):
        """ Working and time is exact minutes """
        data = {
            "days": 1,
            "hours": 0,
            "minutes": 60,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = ''
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_1_day_59_minutes(self):
        """ Working and minutes is < and message not sent """
        data = {
            "days": 1,
            "hours": 0,
            "minutes": 59,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 59 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = ''
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_working_no_status_change_1_day_1_hour(self):
        """ Working and hours are exact """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = ''
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_not_working_no_status_change(self):
        """ Working and hours are exact """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 500
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = ''
        actual_response = create_message(data, one_hour_sent, realm, interval_time, False)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['interval'], 60)

    def test_create_message_status_changed_now_working_debug(self):
        """ Working status changed and he is now working """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 1,
            "seconds": 1,
            "working": True,
            "workingStatusChanged": True,
            "timeLeft": 6458
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '🚨  The Stone Carver has arrived in internville! 🚨\n\nGet those stones quick, before he ' \
                           'heads out on the road again in 1 day 1 hour 1 minute 1 second \n\n#DeFiKingdoms'

        actual_response = create_message(data, one_hour_sent, realm, interval_time, True)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['interval'], 600)

    def test_create_message_status_changed_not_working_debug(self):
        """ Working status changed and he is not working """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 1,
            "seconds": 1,
            "working": False,
            "workingStatusChanged": True,
            "timeLeft": 6458
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = 'He Gone! 🏃‍♂️💨\n\nThe Stone Carver has left! He will be back to internville in 1 day 1 ' \
                           'hour 1 minute 1 second !\n\n #DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, True)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['oneHourMessage'], False)
        self.assertEqual(actual_response['interval'], 600)

    def test_create_message_working_no_status_change_1_hour_debug(self):
        """ Working and hours are exact """
        data = {
            "days": 0,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 60 * 60
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '⏰  One hour left before the Stone Carver leaves! ⏰\n\n#DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, True)

        self.assertEqual(actual_response['message'], expected_message)

    def test_create_message_not_working_no_status_change_debug_true(self):
        """ Working and hours are exact """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": False,
            "workingStatusChanged": False,
            "timeLeft": 500
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = 'Stone Carver will be in internville in 1 day 1 hour \n\n#DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, True)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['interval'], 60)

    def test_create_message_working_no_status_change_debug_true(self):
        """ Working and hours are exact """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": 500
        }
        one_hour_sent = False
        realm = "internville"
        interval_time = 600
        expected_message = '🚨  The Stone Carver in internville! 🚨\n\nGet those stones quick, before he heads out on ' \
                           'the road again in 1 day 1 hour \n\n#DeFiKingdoms'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, True)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['interval'], 60)

    def test_create_message_not_working_ever_debug_true(self):
        """ Working and hours are exact """
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 0,
            "seconds": 0,
            "working": True,
            "workingStatusChanged": False,
            "timeLeft": -1
        }
        one_hour_sent = False
        realm = "Crystalvale 1.0"
        interval_time = 600
        expected_message = 'This StoneCarver has left the realm Crystalvale 1.0 foREVer'
        actual_response = create_message(data, one_hour_sent, realm, interval_time, True)

        self.assertEqual(actual_response['message'], expected_message)
        self.assertEqual(actual_response['interval'], 60)


if __name__ == '__main__':
    unittest.main()
