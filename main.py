import bs4
import requests
import schedule
import time
from time import sleep



def telegram_bot_sendtext(bot_message):

    bot_token = 'your-bot-token-here'
    bot_chatID = 'your-bot-chatID-here'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def check():
    LINK = 'https://www.amazon.it/dp/asin-of-the-product-here'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    res = requests.get(LINK, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    div_case = soup.find('div', id='availability')

    check = str(div_case)

    if "Disponibilità" in check:
        telegram_bot_sendtext("message-to-send")
        print("message-to-print-in-console")
    else:
        print("message-to-print-in-console")


schedule.every(60).minutes.do(check)

while True:

    # running all pending tasks/jobs
    schedule.run_pending()
    time.sleep(1)
