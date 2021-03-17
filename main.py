import os
import schedule
import time
import requests


def send_message(token, chat_id, message):
    url = "https://api.telegram.org/bot"

    if message:
        params = {'chat_id': chat_id, 'text': message}
        response = requests.get(url + token + '/sendMessage', params=params)
    return response


def send_mess():
    message = 'Look at this amazing message!'
    token = os.environ.get('TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    send_message(token, chat_id, message)


def main():
    # schedule
    schedule.every(10).seconds.do(send_mess)
    # run script infinitely
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()

