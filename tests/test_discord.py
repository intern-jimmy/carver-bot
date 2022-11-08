from unittest import TestCase
from unittest.mock import patch
from discord_webhook import DiscordWebhook
from src.discord import sendMessage

class TestDiscord(TestCase):
    @patch.object(DiscordWebhook, 'execute')
    def test_sendMessage(self, webhook):
        sendMessage("Hello World", "www.google.com")
        webhook.assert_called()
        webhook.assert_called_once()