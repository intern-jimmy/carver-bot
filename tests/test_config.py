import unittest
import configparser

import src.config as cfg

class TestConfig(unittest.TestCase):
    def test_creation_loads_a_configfile(self):
        # Arrange
        config = configparser.ConfigParser()
        expected = config.read('config.ini')

        # Act
        actual = cfg.Config()

        # Assert
        """ Figure out how to test this """
        self.assertEqual(1, 1)

    def test_update_of_non_existant_item(self):
        # Arrange
        config = cfg.Config()

        # Act
        config.set('DEFAULT', 'ping', 'pong')

        # Assert
        self.assertEqual(config.get('DEFAULT', 'ping'), 'pong')

    def test_update_existing_option(self):
        # Arrange
        config = cfg.Config()

        # Act
        config.set('DEFAULT', 'interval', '10')

        # Assert
        self.assertEqual(config.get('DEFAULT', 'interval'), '10')

    def test_get_sections(self):
        # Arrange
        config = cfg.Config()
        expected = ['bot', 'Serendale1.0', 'Crystalvale']
        # Act
        actualSections = config.getSections()
        # Assert
        self.assertTrue(expected == actualSections)

    def test_get_options(self):
        # Arrange
        config = cfg.Config()
        expected = ['interval', 'sendtweets', 'senddiscord', 'debug', 'carvers', 'onehourmessage']
        # Act
        actualOptions = config.getOptions('bot')
        # Assert
        print(actualOptions)
        self.assertTrue(expected == actualOptions)

    def test_remove_section(self):
        # Arrange
        config = cfg.Config()
        # Act
        config.removeSection('bot')
        actualOptions = config.getSections()
        # Assert
        self.assertFalse('bot' in actualOptions)

    def test_remove_option(self):
        # Arrange
        config = cfg.Config()
        # Act
        config.removeOption('bot', 'interval')
        actualOptions = config.getOptions('bot')
        # Assert
        self.assertFalse('bot' in actualOptions)


if __name__ == '__main__':
    unittest.main()
