import os
import schedule
import time
import requests


def send_message(message):
    '''
    Takes the chat id of a telegram bot and the text that was  crawled from the
    website and sends it to the bot
    Args: chat_id = string; chat id of the telegram bot,
          text = string; crawled text to be sent
    Returns: None
    '''
    url = "https://api.telegram.org/bot"
    token = os.environ.get('TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    if message:
        params = {'chat_id': chat_id, 'text': message}
        response = requests.get(url + token + '/sendMessage', params=params)
    return response


def send_mess():
    send_message('Look at this amazing message!')


def main():
    # schedule
    schedule.every(10).seconds.do(send_mess)
    # run script infinitely
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()

