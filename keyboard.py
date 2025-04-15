#keyboard.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_keyboard(options):
    keyboard = []
    for option in options:
        keyboard.append([InlineKeyboardButton(option['text'], callback_data=option['next'])])
    return InlineKeyboardMarkup(keyboard)