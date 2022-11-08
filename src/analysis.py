import time
from datetime import datetime

def extractData(carverData, prevCarverData):
    working = carverData['working']

    workingStatusChange = False
    difference = 0
    if not working:
        difference = (carverData["awayUntil"]-carverData["time"])

    else:
        difference = (carverData["workingUntil"]-carverData["time"])
    timeLeft = difference

    days = int(difference/60/60/24)
    difference = difference - (days * 60 * 60 * 24)
    hours = int(difference/60/60)
    difference = difference - (hours * 60 * 60)
    minutes = int(difference/60)
    difference = difference - (minutes * 60)
    seconds = difference

    if not (prevCarverData == None):
        workingStatusChange = working != prevCarverData['working']

    extractedData = {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "working": working,
        "workingStatusChanged": workingStatusChange,
        "timeLeft": timeLeft
    }
    return extractedData

def timeMessage(data):
    message = ''

    if data['days'] > 0:
        message = message + str(data['days'])
        if data['days'] > 1:
            message = message + ' days '
        else:
            message = message + ' day '

    if data['hours'] > 0:
        message = message + str(data['hours'])
        if data['hours'] > 1:
            message = message + ' hours '
        else:
            message = message + ' hour '

    if data['minutes'] > 0:
        message = message + str(data['minutes'])
        if data['minutes'] > 1:
            message = message + ' minutes '
        else:
            message = message + ' minute '

    if data['seconds'] > 0:
        message = message + str(data['seconds'])
        if data['seconds'] > 1:
            message = message + ' seconds '
        else:
            message = message + ' second '
    return message
