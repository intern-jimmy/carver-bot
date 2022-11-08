import os
from dotenv import load_dotenv
from datetime import datetime
import time
import pprint

from config import Config
from commands import Commands
from repeated_timer import RepeatedTimer
from carver import carverAwayUntil, carverWorkingUntil
from analysis import extractData
from messages import create_message
import discord
import twitter

config = None
timedEventLoop = None
previousData = {}
started = ''
checkCount = 0


def main():
    global timedEventLoop
    global started
    started = datetime.now().strftime("%H:%M:%S")
    print('Initializing configuration')
    setup_config()

    """ Generate the event loop """
    timedEventLoop = defineRepeater()

    while True:
        userInput = input("Enter command:\n").split(" ")
        command = userInput[0].upper()
        userInput.pop(0)
        args = userInput

        computeCommands(command, args)


def LogicalCheck():
    """
      1. query the chain to get the stone carvers away and working status
      2. extract data from that
      3. create message
      4. if message not empty send message
      5. save extracted data
    """
    global previousData
    global checkCount
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Starting Check: " + current_time)

    # has to be a better way to deal with a list in a configfile...
    carverRealms = config.get('bot', 'carvers').replace('\'', '').replace('[', '').replace(']', '').replace(' ',
                                                                                                            '').replace(
        '"', '')

    for carverRealm in carverRealms.split(','):
        # realm = carverRealm.strip()
        try:
            data = getCarverData(carverRealm)
            pastData = previousData.get(carverRealm)

            extractedData = extractData(data, pastData)

            print(config.get('bot', 'debug'))
            response_data = create_message(extractedData, config.get('bot', 'oneHourMessage') == 'True', carverRealm, int(config.get('bot', 'interval')),  config.get('bot', 'debug') == 'True')

            if "oneHourMessage" in response_data:
                config.set('bot', 'oneHourMessage', str(response_data['oneHourMessage']))

            if "interval" in response_data:
                config.set('bot', 'interval', str(response_data['interval']))
                updateTime(int(response_data['interval']))

            previousData[carverRealm] = data

            if response_data['message'] != None:
                if config.get('bot', 'sendTweets') == 'True':
                    print(config.get('tweepy', 'apiKey'))
                    print(config.get('tweepy', 'apiSecret'))
                    print(config.get('tweepy', 'accessToken'))
                    print(config.get('tweepy', 'tokenSecret'))

                    twitter.sendTweet(config.get('tweepy', 'apiKey'), config.get('tweepy', 'apiSecret'),
                                      config.get('tweepy', 'accessToken'), config.get('tweepy', 'tokenSecret'), response_data['message'])

                if config.get('bot', 'sendDiscord') == 'True':
                    discord.sendMessage(response_data['message'], config.get('Discord', 'url'))
            else:
                print('No message')
            #  discord.sendMessage('No Message', config.get('Discord', 'url'))
        except Exception as ex:
            print(ex)
            discord.sendMessage('Intern look at the bot: ' + str(ex))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('check complete ' + current_time)
    checkCount = checkCount + 1


def setup_config():
    global config
    """ Get the base config file loaded"""
    config = Config()
    """ Load the secret stuff into the config"""
    load_environment()


def load_environment():
    global config
    load_dotenv()
    """ Load data for Tweepy """
    apiKey = os.getenv('API_KEY')
    apiSecret = os.getenv('API_SECRET')
    bearerToken = os.getenv('BEARER_TOKEN')
    accessToken = os.getenv('ACCESS_TOKEN')
    tokenSecret = os.getenv('TOKEN_SECRET')

    config.addSection('tweepy')
    config.set('tweepy', 'apiKey', apiKey)
    config.set('tweepy', 'apiSecret', apiSecret)
    # config.set('Tweepy', 'bearerToken', bearerToken)
    config.set('tweepy', 'accessToken', accessToken)
    config.set('tweepy', 'tokenSecret', tokenSecret)

    """ Load data for Discord """
    discordUrl = os.getenv('DISCORD_URL')

    config.addSection('Discord')
    config.set('Discord', 'url', discordUrl)


def defineRepeater():
    global config
    return RepeatedTimer(int(config.get('bot', 'interval')), LogicalCheck)


def updateTime(time):
    global timedEventLoop
    timedEventLoop.updateInterval(time)


def computeCommands(command, args):
    global config
    """ Process user input """
    if command == Commands.QUIT.name:
        quit()
    if command == Commands.HELP.name:
        help()
    if command == Commands.DEBUG.name:
        debug(args)
    if command == Commands.INTERVAL.name and len(args) == 0:
        displayInterval()
    if command == Commands.INTERVAL.name and len(args) == 1:
        print(args)
        config.set('bot', 'interval', args[0])
        updateTime(int(config.get('bot', 'interval')))

    if command == Commands.STATUS.name:
        displayStatus()


def getCarverData(carverChain):
    global config
    result = None
    epoch_time = int(time.time())
    try:
        workingUntil = carverWorkingUntil(config.get(carverChain, 'rpc'), config.get(carverChain, 'address'))
        awayUntil = carverAwayUntil(config.get(carverChain, 'rpc'), config.get(carverChain, 'address'))

        result = {"chain": carverChain, "time": epoch_time, "working": epoch_time < workingUntil,
                  "awayUntil": awayUntil, "workingUntil": workingUntil}
    except Exception as e:
        print('oops - ' + str(e))

    return result


def quit():
    global timedEventLoop
    timedEventLoop.stop()
    exit(0)


def help():
    print('exit -> stop the bot\ndebug -> Alerts the next cycle\nTodo: replace with a file')


def debug(args):
    """ Update the debug flag in the config o deplay it """
    global config
    if len(args) > 0:
        config.set('bot', 'debug', args[0])
    else:
        print(config.get('bot', 'debug'))


def displayInterval():
    global config
    print(config.get('bot', 'interval'))


def displayStatus():
    pp = pprint.PrettyPrinter(indent=4)
    global previousData
    global started
    global checkCount
    global config

    print('Start time: ' + started)
    print('Number of checks performed: ' + str(checkCount))
    print('previous data: ' + str(previousData))
    print('config:')
    pp.pprint(config.display())


if __name__ == '__main__':
    main()