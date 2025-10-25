import requests
from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_GOLD_SILVER_CHAT_ID")


def get_gold_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd")
        response.raise_for_status()
        price = response.json()['tether-gold']['usd']
        return price
    except Exception as e:
        print(f"Error fetching price: {str(e)}")
        return None

def get_silver_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=token-teknoloji-a-s-ons-silver&vs_currencies=usd")
        response.raise_for_status()
        price = response.json()['token-teknoloji-a-s-ons-silver']['usd']
        return price
    except Exception as e:
        print(f"Error fetching price: {str(e)}")
        return None

async def send_message(message):
    try:
        if message is not None:
            bot = Bot(token=BOT_TOKEN)
            await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
    except Exception as e:
        print(f"Error sending message: {str(e)}")

if __name__ == "__main__":
    try:
        gold_price = get_gold_price() or 0
        silver_price = get_silver_price() or 0
        asyncio.run(send_message(f"Gold: ${gold_price:.2f}, Silver: ${silver_price:.2f}"))
    except Exception as e:
        print(f"Main loop error: {str(e)}")
