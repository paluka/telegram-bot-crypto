import requests
from telegram import Bot
from dotenv import load_dotenv

import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print(BOT_TOKEN, CHAT_ID)


def get_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    response.raise_for_status()
    price = response.json()['bitcoin']['usd']
    return price

def send_message(price):
    bot = Bot(token=BOT_TOKEN)
    message = f"Current BTC Price: ${price:.2f}"
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    price = get_btc_price()
    send_message(price)
