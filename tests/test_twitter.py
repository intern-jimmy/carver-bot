from unittest import TestCase
from unittest.mock import patch
from src.twitter import sendTweet
import tweepy


class TestTwitter(TestCase):
    @patch.object(tweepy.Client, 'create_tweet')
    def test_sendTweet(self, create_tweet):
        expected_return = 123456789
        create_tweet.return_value = expected_return
        actual_return = sendTweet("test_key", "hush its a secret", "token", "token hush hush", "Test Tweet")
        create_tweet.assert_called()
        create_tweet.assert_called_once()
        create_tweet.assert_called_with(text='Test Tweet', user_auth=True)
        self.assertEqual(actual_return, expected_return) 

