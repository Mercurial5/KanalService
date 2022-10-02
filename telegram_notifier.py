"""
This script is intended to notify orders delivery date.

May be used with crontab.
"""

from sqlalchemy.orm import Session
from dotenv import load_dotenv
from telebot import TeleBot

from datetime import date
from os import getenv

load_dotenv()

from models import Orders, engine


def main():
    bot = TeleBot(getenv('bot_token'))
    chat_id = getenv('chat_id')

    current_date = date.today()

    with Session(engine) as session:
        result = session.query(Orders).filter_by(date=current_date).all()
        for row in result:
            # You could add more details here, but I thought it's not necessary.
            bot.send_message(chat_id, f'Order no. {row.id} delivery date is today!')


if __name__ == '__main__':
    main()
