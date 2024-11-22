import requests
from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def get_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=daddy-tate&vs_currencies=usd")
    response.raise_for_status()
    price = response.json()['daddy-tate']['usd']
    return price

async def send_message(price):
    bot = Bot(token=BOT_TOKEN)
    message = f"${price:.5f}"
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)

if __name__ == "__main__":
    price = get_btc_price()
    asyncio.run(send_message(price))
