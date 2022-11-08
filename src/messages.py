from analysis import timeMessage


def create_message(data, one_hour_sent, realm, interval_time, debug):
    message = None
    response_data = {'message': ''}
    '''
  * working status changed && working
      * send out Carver is here
      *replace interval time to .env
  * working status changes && !Working
      * Send out See you in * time
  * !working status changed && !working
      * timeLeft < interval
          * lower interval on checking
  * !workingStatus changed && working
      * timeLeft ~ 1 hour
          *send one hour warning
  * debug
      Send a status
  '''
    timestamp = timeMessage(data)

    # check for the stone carver just setting up shop
    if data['workingStatusChanged'] and data['working']:
        message = '🚨  The Stone Carver has arrived in ' + realm + '! 🚨\n\nGet those stones quick, before he heads ' \
                                                                  'out on the road again in ' + \
                  timestamp + '\n\n#DeFiKingdoms'
        response_data['interval'] = 600  # maybe take this in to
        response_data['message'] = message
    # check if the stone carver just left
    if data['workingStatusChanged'] and not data['working']:
        message = 'He Gone! 🏃‍♂️💨\n\nThe Stone Carver has left! He will be back to ' + realm + ' in ' + \
                  timestamp + '!\n\n #DeFiKingdoms'
        response_data['oneHourMessage'] = False
        response_data['message'] = message
        response_data['interval'] = 600  # reset interval
    # check to see if the carver is about to leave
    if (not data['workingStatusChanged']
            and data['working']
            and not one_hour_sent
            and data['days'] == 0
            and ((data['hours'] == 0 and data['minutes'] <= 60) or (data['hours'] == 1 and data['minutes'] == 0))):
        response_data['oneHourMessage'] = True
        message = '⏰  One hour left before the Stone Carver leaves! ⏰\n\n#DeFiKingdoms'
        response_data['message'] = message

    # check to see if the interval needs to be updated to accurately find him
    if response_data['message'] == '':
        # update to check once a minute
        if interval_time > 60 and data['timeLeft'] < interval_time:
            # update interval to check every minute
            response_data['interval'] = 60

    if debug and message is None:
        if data['timeLeft'] > 0:
            message = '🚨  The Stone Carver in ' + realm + '! 🚨\n\nGet those stones quick, before he heads out on ' \
                                                          'the road again in ' if \
                data['working'] else 'Stone Carver will be in ' + realm + ' in '
            message = message + timestamp + '\n\n#DeFiKingdoms'
        else:
            message = 'This StoneCarver has left the realm ' + realm + ' foREVer'
        response_data['message'] = message

    return response_data
