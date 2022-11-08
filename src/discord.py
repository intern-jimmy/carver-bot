from discord_webhook import DiscordWebhook

def sendMessage(message, url):
  webhook = DiscordWebhook(url=url, content=message)
  webhook.execute()