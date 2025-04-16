# keyboard.py
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def build_keyboard(options):
    keyboard = []
    for option in options:
        if 'next' in option:
            callback_data = option['next']
        elif 'callback_data' in option:
            callback_data = option['callback_data']
        else:
            continue  # пропустить, если нет нужных ключей

        keyboard.append([InlineKeyboardButton(option['text'], callback_data=callback_data)])
    return InlineKeyboardMarkup(keyboard)